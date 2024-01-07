from pdf2docx import Converter

def pdf2docxUtil(pdf_path):
    # 生成DOCX文件的路径
    print("pdf_path:",pdf_path)
    docx_path = pdf_path.replace('.pdf', '.docx')
    print("docx_path:",docx_path)
    # 使用pdf2docx库将PDF转换为DOCX
    cv = Converter(pdf_path)
    cv.convert(docx_path, start=0, end=None)
    print(docx_path)
    cv.close()
    return docx_path

