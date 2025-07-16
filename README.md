# Capstone-Project-Module-1
## Business Overview

This program is made for the purpose of helping medical staffs to organize patients data in a hospital. Medical staff will be able too see the current patients in medical care provided by the table created in this program.

## Program Features:
The  main feature of this program includes :
A. Create
B. Read
C. Update
D. Delete

with the extra features include a role based login system.
A. Create
The create feature is for adding patients data to list of datas. User will be asked to input the id, name, diagnosis and the facilities used by the patient. Additional feature of create include a notification system if similiar id is used.

B. Read
The read feature is for overseeing the data list for the medical staff to review it by revealing the full patient data list. The data shown includes ID, Name, Diagnosis and Medical Facilities used

C. Update
The update feature is used for updating some parts of the data. The data that can be manipulated by the feature includes diagnosis and facilities used.

D. Delete
The delete feature is used for removing patients data that is not in hospital care anyomre. The feature works by inputing the patients id, which will delete the whole data related to the id.

## Instruction on How to Use
if not installed already, please install the tabulate feature first. the installation can be done using the terminal in visual studio code and then input the following : - pip install tabulate
1. Run the program
2. Input the ID and Password required (user can use (01) and (qwerty1234) for doctor role and (02) and (abcdefg) for admin role)
3. User will be redirected to the main menu with the following menu shown corresponding the role 
For doctor role, user can choose the following : 
1. Tampilkan data pasien (show patients data)
2. Tambahkan data pasien (add patients data)
3. Perbarui data pasien (update patients data)
5. Log Out
6. Exit

For admin role, an additional menu will be shown, which is 4. Hapus data pasien (Delete patients data)
inputing the number 1 will open the patients data table, where user can see the ID, Name, Diagnosis, and the facilities used by the patient.
Inputing the number 2 will add a new patient data. User will be asked to input the following :
- ID
- Name
- Diagnosis
- Facilities Used
inputing the number 3 will update patient data. User will be asked to input the ID of patient. if succesful, user will be asked which data that will be updated. The data that can be updated is diagnosis and facilities used.
If user signed in as admin, user can input number 4 to delete a data. User will be requested the ID of patient that will be deleted. if the ID is available on the data list, the patients data with the ID specified will be removed.
inputing the number 5 will log the user off, and return to login page
inputing the number 6 will shut down the program.
