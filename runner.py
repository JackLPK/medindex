from pathlib import Path
import sys

project_path = Path(__file__).parent.absolute()
gui_dir = Path(project_path, 'gui')
db_dir = Path(project_path, 'database')
db_path = Path(db_dir,  'meds.db')
html_template_path = Path(gui_dir, 'webview', 'template.html')
html_out_path = Path(gui_dir, 'webview', 'out.html')

# 
my_paths = {'db': db_path, 
            'template': html_template_path, 
            'out': html_out_path}

# 
sys.path.append(str(gui_dir))
sys.path.append(str(db_dir))

# 
import gui_start

gui_start.main(my_paths)



