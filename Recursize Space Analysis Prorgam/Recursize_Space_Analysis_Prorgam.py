
"""
Recursize Space Analysis Prorgam Version 1.00
=============================================

I wrote this program to help me manage my disk space.  This program identifies the amount of space included in a given directory, 
including sub-directories.

Three parameters are set in Main :
   1.) directory_to_analyze
   2.) units_of_measure
   3.) min_size_to_display   

The program determines the size of the directory_to_analyze.  If sub-directories exist they are recursively analyzed.  Once
the size of a directory is determined, the directory and amount of space is displayed if the amount of space is equal to or
greater than the min_size_to_display.

In the past have not used python to access directory file lists.  I used google to search for such information and came accross a simple 
recursize routine to traverse directories.  I modified that routine by adding code to identify file sizes and to bubble
up that information through recursive calls for my purposes.  

"""

import os, sys
from stat import *
from datetime import date

def traverse_directory(dir_to_process,units_of_measure,min_size_to_display):
    
    try:
        list_files_directories=os.listdir(dir_to_process)
    except Exception as inst:
        dir_err_no, dir_err_msg = inst.args
        print(f"Error processing this directory : {dir_to_process}.")
        input(f"{dir_err_msg}.  Press any key to continue.")
        return 0
    
    space_used_directory=0.0
    for file_or_dir in list_files_directories:
        pathname = os.path.join(dir_to_process, file_or_dir)
        mode = os.lstat(pathname).st_mode

        if S_ISDIR(mode):
            space_used_directory += traverse_directory(pathname,units_of_measure,min_size_to_display)
        elif S_ISREG(mode):
            file_size=determine_file_size(pathname,units_of_measure)
            space_used_directory += file_size
        else:
            print('Unknown file type - skipping %s' % pathname)
            
    if (min_size_to_display <= space_used_directory):
        print(f"Spaced used in directory {dir_to_process} is {space_used_directory:,.2f} in {units_of_measure}.")
        
    return space_used_directory

def determine_file_size(pathname,units_of_measure):
    file_stats = os.stat(pathname)
    file_size_calc=file_stats.st_size
    if (units_of_measure=="MB"):
        file_size_calc /= 1024**2
    elif (units_of_measure=="GB"):
        file_size_calc /= 1024**3
    return file_size_calc

if __name__ == '__main__':
    directory_to_analyze="C:\\Users\\Telesis\\Documents"  
    directory_to_analyze="C:\\Users\\Telesis\\Pictures\\2022" 
    units_of_measure="GB"
    min_size_to_display=10   
    
    print("Recursize Space Analysis Prorgam Version 1.00")
    print("=============================================")
    print(f"Directory to analyze : {directory_to_analyze}")
    print(f"Units of measuer : {units_of_measure}")
    print(f"Minimum size to display : {min_size_to_display} {units_of_measure}")
    print("Run date : ",date.today(),"\n")

    traverse_directory(directory_to_analyze,units_of_measure,min_size_to_display)   
    
    print("\nDone")
    
