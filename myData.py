import searchTable as st

entries = [st.Entry("Professor Messer CompTIA A+ Course","https://www.youtube.com/playlist?list=PLG49S3nxzAnnOmvg5UGVenB_qQgsh01uC","A youtube playlist of CompTIA A+ prep videos.",["CompTIA","IT"]),
st.Entry("USDA Fern Page","https://www.fs.usda.gov/wildflowers/beauty/ferns/what.shtml","A USDA webpage describing ferns.",["ferns","plants"])]

myTable = st.SearchTable(entries)
