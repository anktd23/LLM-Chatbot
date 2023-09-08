import os
from textExtractor import textExtract,saveTextToFile,txtFileMerger,textExtractPyPDF
from config import file_path_input,file_path_output,file_path_merged

if __name__ =="__main__":
    # text = textExtract(file_path_input)
    # txtfile = saveTextToFile(text, file_path_output,output_file_name)
    
    for input_file_name in os.listdir(file_path_input):
        if input_file_name.endswith('.pdf'):
            input_file_path = os.path.join(file_path_input, input_file_name)
            text = textExtract(input_file_path)
            #text = textExtractPyPDF(input_file_path)
            output_text_file = os.path.splitext(input_file_name)[0] + '.txt'
            saveTextToFile(text, file_path_output, output_text_file)
    txtFileMerger(file_path_output, file_path_merged )

