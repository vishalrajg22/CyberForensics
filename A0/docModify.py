import aspose.words as aw

# create document object
doc = aw.Document("document.docx")

builder = aw.DocumentBuilder(doc)

# manipulate document
builder.write("world")

# save document
doc.save("document.docx")
