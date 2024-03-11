import yaml
import os

# BASE_URLという環境変数を読み込む
def get_base_url():
    return os.environ['BASE_URL'] + '/blob/main'

# rules/sigma/ディレクトリにあるymlファイルをすべて読み込む
def load_yaml_files():
    sigma_dir = 'rules/sigma'
    splunk_dir = 'rules/splunk'
    splunk_extention = '.spl'

    yamls = []
    files = os.listdir(sigma_dir)
    for file in files:
        with open(sigma_dir + '/' + file, 'r') as f:
            content = yaml.safe_load(f)
            content['paths'] = {
                'sigma': get_base_url() + '/' + sigma_dir + '/' + file,
                'splunk': get_base_url() + '/' + splunk_dir + '/' + file.replace('.yml', splunk_extention)
                }
            yamls.append(content)
    return yamls

# すべてのymlファイルを読み込んで、それらをdataという名前に対応する辞書に格納する
def format_output_data():
    data = {'data': load_yaml_files()}
    return data

# 出力するデータをファイルに書き出す
def write_output_data(data):
    with open('src/data/rules.yml', 'w') as f:
        yaml.dump(data, f)

# メイン関数
def main():
    data = format_output_data()
    write_output_data(data)

if __name__ == '__main__':
    main()
