import FreeSimpleGUI as fsg

labelOne = fsg.Text("Select files to Compress")
input_box = fsg.Input()
choose_button = fsg.FileBrowse("Choose File(s)")

labelTwo = fsg.Text("Select Destination Folder")
input_box2 = fsg.Input()
choose_button2 = fsg.FolderBrowse("Choose Folder")

compress_btn = fsg.Button("Compress")

window = fsg.Window("File Compressor",
                    layout=[[labelOne,input_box, choose_button],
                            [labelTwo,input_box2, choose_button2],
                            [compress_btn]])

window.read()
window.close()