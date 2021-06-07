from cx_Freeze import setup, Executable

includeFile=[("sources/screenshots/diagnosis.png","sources/screenshots/diagnosis.png"),("sources/screenshots/patientRecord.png","sources/screenshots/patientRecord.png"),("sources/screenshots/serviceRecord.png","sources/screenshots/serviceRecord.png"),("sources/setting.png","sources/setting.png"),("sources/imageedit_10_5975279466.png","sources/imageedit_10_5975279466.png"),("sources/logo.png","sources/logo.png")]

setup(name="Hospital Management System",
      version="0.1",
      description="Jae Hyeok's practice Hospital Management System",
      options={'build_exe':{'include_files':includeFile}},
      executables=[Executable("home.py")])