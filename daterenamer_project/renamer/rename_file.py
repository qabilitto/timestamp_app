from datetime import  datetime
import os
import logging

logger=logging.getLogger(__name__)

class DateRenamer:
    def __init__(self,filename):
        self.filename=filename
    
    def rename_it(self):
        get_date = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
        extract_filename = os.path.basename(self.filename)
        extract_dirname = os.path.dirname(self.filename)
        new_file_name = get_date + '_' +extract_filename
        logger.debug('Okay trying to rename given file')
        os.rename(self.filename,os.path.join(extract_dirname,new_file_name))