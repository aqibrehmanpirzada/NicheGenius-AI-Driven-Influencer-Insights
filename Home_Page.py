import streamlit as st

def main():
    # Inject custom CSS for sidebar and main content styling
    st.markdown(
        """
        <style>
        /* Sidebar styles */
        div[data-testid="stSidebar"] {
            background-color: #007BFF;  /* Blue background color */
            color: #ffffff;  /* White text color */
        }
        div[data-testid="stSidebar"] a {
            color: #ffffff;  /* White links */
        }
        div[data-testid="stSidebar"] .stButton > button {
            color: #ffffff;
            background-color: #0056b3;  /* Darker blue for buttons */
        }

        /* Main title styling */
        .title {
            font-size: 3em;
            text-align: center;
            padding-bottom: 20px;
            animation: glow 2s linear infinite alternate;
            text-shadow: 0 0 10px #007BFF, 0 0 20px #007BFF, 0 0 30px #007BFF, 0 0 40px #0056b3, 0 0 70px #0056b3, 0 0 80px #0056b3, 0 0 100px #0056b3, 0 0 150px #0056b3;
        }

        /* Animation for glowing effect */
        @keyframes glow {
            from {
                text-shadow: 0 0 10px #007BFF, 0 0 20px #007BFF, 0 0 30px #007BFF, 0 0 40px #0056b3, 0 0 70px #0056b3, 0 0 80px #0056b3, 0 0 100px #0056b3, 0 0 150px #0056b3;
            }
            to {
                text-shadow: 0 0 20px #007BFF, 0 0 30px #007BFF, 0 0 40px #0056b3, 0 0 70px #0056b3, 0 0 80px #0056b3, 0 0 100px #0056b3, 0 0 150px #0056b3, 0 0 200px #0056b3, 0 0 300px #0056b3;
            }
        }

        /* Beautify table */
        table {
            border-collapse: collapse;
            width: 100%;
            margin-bottom: 20px;
        }
        th, td {
            padding: 12px;
            text-align: left;
            border: 1px solid #ddd;
        }
        th {
            background-color: #0056b3; /* Dark blue background for header */
            color: #ffffff; /* White text color for header */
            font-weight: bold;
        }
        # tr:nth-child(even) {
        #     background-color: #f2f2f2; /* Light gray for even rows */
        # }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display the title with the custom class
    st.markdown("<h3 class='title'>💡Realtime Influencer Recommendation Engine For Niche Marketing💡</h3>", unsafe_allow_html=True)

    st.markdown("""
        Welcome to our App! Brands often miss the right influencers who resonate with niche
        audiences, resulting in ineffective and broad campaigns. We created a 
        recommendation system that finds influencers aligned with a brand's values, target 
        demographic, and desired campaign tone in real time, offering authentic connections with 
        engaged audiences.
        """)

    st.markdown('---')

    st.markdown(
        """
        <table>
            <thead>
                <tr>
                    <th>Feature</th>
                    <th>Description</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Upload PDF Documents of your Business</strong></td>
                    <td>Upload your PDF files for business analysis and get your recommendation accordingly.</td>
                </tr>
                <tr>
                    <td><strong>Dashboard Analysis</strong></td>
                    <td>Extract data and get recommendations based on your Business Dashboards.</td>
                </tr>
                <tr>
                    <td><strong>General Discussion</strong></td>
                    <td>Discuss your business and get recommendations based on your specific niche.</td>
                </tr>
            </tbody>
        </table>
        """,
        unsafe_allow_html=True
    )

    st.markdown('---')

    st.subheader('How to Use:')
    st.markdown("""
    1. Upload your Business Document PDF file using the file uploader.
    2. Our app will automatically process the uploaded Dashboard to get analysis and recommendations.
    3. Discuss the Problems with Business Assistant and get recommendations.
    """)

if __name__ == '__main__':
    main()
