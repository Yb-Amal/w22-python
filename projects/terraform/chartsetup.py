import shutil 

shutil.copy('projects/chart.yml', 'projects/chart_bk.yml')

def chartModif(chart_version):
    with open("projects/chart.yml", 'r') as f:
        content = f.readlines()
        
    with open("projects/chart.yml" , 'w')  as f1:
        for line in content:
            if 'version' in line:
                f1.write(f'version: {chart_version}\n')
            else:
                f1.write(line)
     
chartModif('3.0')    