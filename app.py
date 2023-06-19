from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import zipfile
from tool import data_processing, inverted_indexes, document_frequency, displaycut
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './temp'
# file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

@app.route('/')
def search():
    return render_template('search.html')


@app.route('/result', methods=['POST'])
def result():
    # 获取用户输入的关键词和返回的文档数
    keyword = request.form['keyword']
    num = int(request.form['num'])

    # 保存用户上传的文件
    file = request.files['file']
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)  # 将文件保存在指定的上传文件夹下

        # 解压用户上传的 .zip 文件
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall('uploaded_folder')

    # 创建倒排索引
    inverted_indexes.create('uploaded_folder')

    # 计算文档频率
    doc_freq = document_frequency.calculate('uploaded_folder')

    # 检索相关文档
    results = inverted_indexes.search(keyword, doc_freq, num)

    # 准备结果页面需要的数据
    data = []
    for result in results:
        # 分词并标注词性
        seg_result, pos_img = displaycut.cut_and_tag(result['content'])
        print("results ==>",seg_result)

        data.append({
            'title': result['title'],
            'segmentation': ' '.join(seg_result),
            'part_of_speech_img': pos_img
        })
    # 打印关键变量
    print("keyword ==>",keyword)
    print("doc_freq ==>",doc_freq)
    print("data ==>",data)

    return render_template('result.html', results=data)




if __name__ == '__main__':
    app.run(debug=True)
