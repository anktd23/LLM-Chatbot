import fitz,sys,os
from PyPDF2 import PdfReader
from exception import LLMException
from logger import logging

def textExtract(file_path_input: str)->str:
    '''
    This function extract text from given pdf document
    ==============================================================
    input_params -> input path file path :str
    outputs -> str
    ===============================================================
    '''
    try:
        logging.info(f"Opening pdf document{file_path_input}")
        doc = fitz.open(file_path_input)
        all_txt = ""
        for page in doc:
            text = page.get_text()
            text = text.strip()
            all_txt = all_txt + text
        all_txt = ' '.join(all_txt.split())
        doc.close()
        logging.info(f"Text extraction completed")
        return all_txt
    except Exception as e:
        raise LLMException(e, sys)

def saveTextToFile(text: str, output_directory: str, output_file_name: str):
    '''
    This function save extracted text from given pdf document to text document
    ==========================================================================
    input_params -> text :str, output file path :str, outfile file name : str
    outputs -> text file
    ==========================================================================
    '''
    try:
        logging.info(f"Creating output directory path")
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
        
        output_file_path = os.path.join(output_directory, output_file_name)
        logging.info(f"Reading extracted text")
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(text)
            file.close()
        logging.info(f"pdf document saved in .txt file format {output_file_path}")  
    except Exception as e:
        raise LLMException(e, sys)

def txtFileMerger(file_path_output :str,file_path_merged :str):     
    '''
    This function merges text documents.
    ==========================================================================
    input_params -> file_path_output :str,file_path_merged :str
    outputs -> text file
    ==========================================================================
    '''
    try:
        logging.info(f"List all the .txt files in the input folder {file_path_output}")
        txt_files = [file for file in os.listdir(file_path_output) if file.endswith('.txt')]

        logging.info(f"Creating output directory path")
        if not os.path.exists(file_path_merged):
            os.makedirs(file_path_merged)

        logging.info(f"Read the content of each .txt file and merge them")
        merged_text = ''
        for txt_file in txt_files:
            txt_file_path = os.path.join(file_path_output, txt_file)
            with open(txt_file_path, 'r', encoding='utf-8') as file:
                merged_text += file.read() + '\n'
                file.close()

        logging.info(f"Write the merged content to the output file")
        merged_file_path = os.path.join(file_path_merged, 'merged_doc.txt')
        with open(merged_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(merged_text)
            output_file.close()
        logging.info(f"merged_doc.txt saved to {merged_file_path}")
        return merged_file_path
    except Exception as e:
        raise e

# def textExtractPyPDF(file_path_input: str)->str:
#     '''
#     This function extract text from given pdf document
#     ==============================================================
#     input_params -> input path file path :str
#     outputs -> str
#     ===============================================================
#     '''
#     try:
#         logging.info(f"Opening pdf document{file_path_input}")
#         doc = PdfReader(file_path_input)
#         page = doc.pages[0]
#         text = page.extract_text()
#         text = text.strip()
#         logging.info(f"Text extraction completed")
#         return text
#     except Exception as e:
#         raise LLMException(e, sys)
    
def textExtractPyPDF(file_path_input: str) -> str:
    '''
    This function extracts text from a given pdf document
    ==============================================================
    input_params -> input path file path :str
    outputs -> str
    ===============================================================
    '''
    try:
        logging.info(f"Opening pdf document {file_path_input}")
        doc = PdfReader(file_path_input)
        text = ""

        for page in doc.pages:
            text += page.extract_text()

        text = text.strip()
        logging.info(f"Text extraction completed")
        return text
    except Exception as e:
        raise LLMException(e, sys)
