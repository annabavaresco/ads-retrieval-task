from flask import Flask, render_template, request
from utils import *



annot_df = AnnotDf('annotations/ranking_annotations.csv')
start_idx = annot_df.resume()
annot_manager = AnnotationManager(annot_df)
annot_manager.current_index = start_idx
app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def index():

    image_path = annot_manager.get_image_path()
    image_id = annot_manager.get_image_name()
    statement = annot_df.get_statement(annot_manager.current_index)
    im_url = annot_manager.get_image_url()

    # print(image_path)
    return render_template('index_range.html', image_path=image_path, image_id = image_id, 
                            image_url = im_url, statement=statement)

@app.route('/annotate', methods=['post'])
def annotate():

    answer = request.form.get('rating')
    annot_df.annotate_ans_ranking(answer, annot_manager.current_index)
    annot_manager.current_index += 1
    if annot_manager.current_index != len(annot_manager.image_paths):
        image_path = annot_manager.get_image_path()
        image_id = annot_manager.get_image_name()
        statement = annot_df.get_statement(annot_manager.current_index)
        im_url = annot_manager.get_image_url()

        return render_template('index_range.html', image_path=image_path, image_id = image_id, 
                               image_url = im_url, statement=statement)
    else:
        return render_template('end.html')

@app.route('/back')

def back():
    if annot_manager.current_index != 0:
        annot_manager.current_index -= 1
        
    image_path = annot_manager.get_image_path()
    image_id = annot_manager.get_image_name()
    statement = annot_df.get_statement(annot_manager.current_index)
    im_url = annot_manager.get_image_url()

    return render_template('index_range.html', image_path=image_path, image_id = image_id, 
                            image_url = im_url, statement=statement)

@app.route('/next')

def next():
    annot_manager.current_index += 1
    if annot_manager.current_index != len(annot_manager.image_paths):
        image_path = annot_manager.get_image_path()
        image_id = annot_manager.get_image_name()
        statement = annot_df.get_statement(annot_manager.current_index)
        im_url = annot_manager.get_image_url()

        print('got here')
        return render_template('index_range.html', image_path=image_path, image_id = image_id, 
                               image_url = im_url, statement=statement)
    else:
        return render_template('end.html')


if __name__ == '__main__':
    app.run(debug=True)
