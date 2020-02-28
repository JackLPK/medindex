from pathlib import Path
import sys
from medindex.gui import gui_start

def run():
    print('runner: im running!')

    project_path = Path(__file__).parent.absolute()
    gui_dir = Path(project_path, 'gui')
    db_dir = Path(project_path, 'database')

    db_path = Path(db_dir,  'MedIndex.db')
    html_template_path = Path(gui_dir, 'webview', 'template.html')
    html_out_path = Path(gui_dir, 'webview', 'out.html')

    # 
    my_paths = {'db': str(db_path), 
                'template': str(html_template_path), 
                'out': str(html_out_path)}

    # 
    # sys.path.append(str(gui_dir))
    # sys.path.append(str(db_dir))

    # 
    gui_start.run(my_paths)




