from pdf2image import convert_from_path
 
 
paths = ["results_eval/results_eval/results_eval/episode-level/plots/overview_in01.pdf"]

# Store Pdf with convert_from_path function
images = convert_from_path(paths[0])
images[0].save('results_eval/results_eval/results_eval/episode-level/plots/overview_in01.jpg', 'JPEG')