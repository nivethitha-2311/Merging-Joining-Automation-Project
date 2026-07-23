import streamlit as st
import pandas as pd

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Data Merging & Joining",
    page_icon="🔗",
    layout="wide"
)

st.title("🔗 Data Merging and Joining")
st.write("Upload two CSV files and perform Merge or Join operations.")

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.title("Operations")

operation = st.sidebar.selectbox(
    "Select Operation",
    [
        "Merging",
        "Joining"
    ]
)

# --------------------------------------------------
# File Upload
# --------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    file1 = st.file_uploader(
        "Upload First CSV File",
        type=["csv"],
        key="file1"
    )

with col2:
    file2 = st.file_uploader(
        "Upload Second CSV File",
        type=["csv"],
        key="file2"
    )

# --------------------------------------------------
# Read Files
# --------------------------------------------------

if file1 is not None and file2 is not None:

    try:

        df1 = pd.read_csv(file1, encoding="latin1")
        df2 = pd.read_csv(file2, encoding="latin1")

        st.success("✅ Both Files Loaded Successfully")

    except Exception as e:

        st.error(e)
        st.stop()

    # ----------------------------------------------
    # Dataset Preview
    # ----------------------------------------------

    st.subheader("📄 First Dataset")

    st.dataframe(df1.head())

    st.write("Shape :", df1.shape)

    st.subheader("📄 Second Dataset")

    st.dataframe(df2.head())

    st.write("Shape :", df2.shape)

    # ----------------------------------------------
    # Common Columns
    # ----------------------------------------------

    common_columns = [
        col for col in df1.columns
        if col in df2.columns
    ]

    if len(common_columns) == 0:

        st.error("❌ No Common Columns Found")

        st.stop()

    st.subheader("✅ Common Columns")

    st.write(common_columns)

    selected_column = st.selectbox(
        "Select Common Column",
        common_columns
    )

    # --------------------------------------------------
    # MERGING
    # --------------------------------------------------

    if operation == "Merging":

        st.header("🔀 Data Merging")

        merge_type = st.selectbox(
            "Select Merge Type",
            [
                "inner",
                "outer",
                "left",
                "right"
            ]
        )

        if st.button("Perform Merge"):

            try:

                result = pd.merge(
                    df1,
                    df2,
                    on=selected_column,
                    how=merge_type
                )

                st.success(
                    f"✅ {merge_type.capitalize()} Merge Completed Successfully"
                )

                st.subheader("Merged Dataset")

                st.dataframe(result)

                st.write("Shape :", result.shape)

                csv = result.to_csv(index=False).encode("utf-8")

                st.download_button(
                    label="⬇ Download Merged CSV",
                    data=csv,
                    file_name=f"{merge_type.capitalize()}_Merged.csv",
                    mime="text/csv"
                )

            except Exception as e:

                st.error(e)

    # --------------------------------------------------
    # JOINING
    # --------------------------------------------------

    elif operation == "Joining":

        st.header("🔗 Data Joining")

        join_type = st.selectbox(
            "Select Join Type",
            [
                "inner",
                "outer",
                "left",
                "right"
            ]
        )

        if st.button("Perform Join"):

            try:

                df1_index = df1.set_index(selected_column)
                df2_index = df2.set_index(selected_column)

                result = df1_index.join(
                    df2_index,
                    how=join_type,
                    lsuffix="_File1",
                    rsuffix="_File2"
                )

                result = result.reset_index()

                st.success(
                    f"✅ {join_type.capitalize()} Join Completed Successfully"
                )

                st.subheader("Joined Dataset")

                st.dataframe(result)

                st.write("Shape :", result.shape)

                csv = result.to_csv(index=False).encode("utf-8")

                st.download_button(
                    label="⬇ Download Joined CSV",
                    data=csv,
                    file_name=f"{join_type.capitalize()}_Joined.csv",
                    mime="text/csv"
                )

            except Exception as e:

                st.error(e)

    # --------------------------------------------------
    # SIDEBAR DATASET INFORMATION
    # --------------------------------------------------

    st.sidebar.markdown("---")
    st.sidebar.subheader("📊 Dataset Information")

    st.sidebar.write("### First Dataset")
    st.sidebar.write(f"Rows : {df1.shape[0]}")
    st.sidebar.write(f"Columns : {df1.shape[1]}")

    st.sidebar.write("### Second Dataset")
    st.sidebar.write(f"Rows : {df2.shape[0]}")
    st.sidebar.write(f"Columns : {df2.shape[1]}")

    st.sidebar.markdown("---")

    # --------------------------------------------------
    # DATASET STATISTICS
    # --------------------------------------------------

    if st.sidebar.checkbox("📈 Show Dataset Statistics"):

        st.subheader("📈 First Dataset Statistics")
        st.dataframe(df1.describe(include="all"))

        st.subheader("📈 Second Dataset Statistics")
        st.dataframe(df2.describe(include="all"))

    # --------------------------------------------------
    # MISSING VALUES
    # --------------------------------------------------

    if st.sidebar.checkbox("⚠ Show Missing Values"):

        st.subheader("⚠ Missing Values - First Dataset")

        missing1 = (
            df1.isnull()
               .sum()
               .reset_index()
               .rename(columns={
                   "index": "Column",
                   0: "Missing Values"
               })
        )

        st.dataframe(missing1)

        st.subheader("⚠ Missing Values - Second Dataset")

        missing2 = (
            df2.isnull()
               .sum()
               .reset_index()
               .rename(columns={
                   "index": "Column",
                   0: "Missing Values"
               })
        )

        st.dataframe(missing2)

    # --------------------------------------------------
    # DATA TYPES
    # --------------------------------------------------

    if st.sidebar.checkbox("📋 Show Data Types"):

        st.subheader("📋 First Dataset Data Types")

        dtype1 = (
            df1.dtypes
               .astype(str)
               .reset_index()
               .rename(columns={
                   "index": "Column",
                   0: "Data Type"
               })
        )

        st.dataframe(dtype1)

        st.subheader("📋 Second Dataset Data Types")

        dtype2 = (
            df2.dtypes
               .astype(str)
               .reset_index()
               .rename(columns={
                   "index": "Column",
                   0: "Data Type"
               })
        )

        st.dataframe(dtype2)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.markdown(
    """
    <div style='text-align:center'>
        <h3>🔗 Data Merging & Joining Mini Project</h3>
        <p>Developed using <b>Python • Pandas • Streamlit</b></p>
    </div>
    """,
    unsafe_allow_html=True
)