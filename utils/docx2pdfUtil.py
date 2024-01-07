from docx2pdf import convert

def convert_docx_to_pdf(input_path, output_path):
    try:
        # 使用docx2pdf库进行转换
        convert(input_path, output_path)
        print(f"转换成功，结果保存在: {output_path}")
    except Exception as e:
        print(f"转换失败: {str(e)}")

if __name__ == "__main__":
    # 用户输入文件路径
    input_file_path = input("请输入.docx文件的路径: ")

    # 指定输出目录
    output_directory = input("请输入保存结果的目录: ")

    # 构建输出文件路径
    output_file_path = f"{output_directory}/output.pdf"

    # 执行转换
    convert_docx_to_pdf(input_file_path, output_file_path)
