import streamlit as st

from project.geohash import GeoPrecision, Latitude, Longitude, decode, encode


def main():
    """Streamlit geohash encoder/decoder app"""

    st.markdown(
        """
        <h1 style='text-align: center; font-size: 65px; color: #4682B4'>
        Geohash Encoder/Decoder</h1
        """,
        unsafe_allow_html=True,
    )

    # Encoding
    lat = st.number_input("Latitude", Latitude.ge, Latitude.le)
    lon = st.number_input("Longitude", Longitude.ge, Longitude.le)
    precision = st.number_input("Precision", GeoPrecision.ge, GeoPrecision.le, 12)

    if st.button("Encode"):
        result = encode(lat, lon, precision)
        st.success(result)

    # Decoding
    geohash = st.text_input("Geohash", "dqcjqcpeqtpg", max_chars=GeoPrecision.le)
    if st.button("Decode"):
        result = decode(geohash)
        st.success(result)


if __name__ == "__main__":
    main()
