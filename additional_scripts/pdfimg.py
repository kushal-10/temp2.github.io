# CONVERT PDF TO JPG

from pdf2image import convert_from_path
 
#ALL, PV/SH,  REF, IMAGE, TABOO, WORDLE, 
paths = ["results_eval/results_eval/results_eval/episode-level/plots/lines.pdf",
         "results_eval/results_eval/privateshared/results_eval/episode-level/plots/privateshared_overview-lines.pdf",
         "results_eval/results_eval/referencegame/results_eval/episode-level/plots/referencegame_overview-lines.pdf",
         "results_eval/results_eval/imagegame/results_eval/episode-level/plots/imagegame_overview-lines.pdf",
         "results_eval/results_eval/taboo/results_eval/episode-level/plots/taboo_overview-lines.pdf",
         "results_eval/results_eval/wordle/results_eval/episode-level/plots/wordle_overview-lines.pdf",
         "results_eval/results_eval/wordle_withclue/results_eval/episode-level/plots/wordle_withclue_overview-lines.pdf",
         "results_eval/results_eval/wordle_withcritic/results_eval/episode-level/plots/wordle_withcritic_overview-lines.pdf"
         ]

img_paths = ["_posts/plots/lines.jpg",
         "_posts/plots/privateshared_overview-lines.jpg",
         "_posts/plots/referencegame_overview-lines.jpg",
         "_posts/plots/imagegame_overview-lines.jpg",
         "_posts/plots/taboo_overview-lines.jpg",
         "_posts/plots/wordle_overview-lines.jpg",
         "_posts/plots/wordle_withclue_overview-lines.jpg",
         "_posts/plots/wordle_withcritic_overview-lines.jpg"
         ]

# Store Pdf with convert_from_path function
for i in range(len(paths)):
    images = convert_from_path(paths[i])
    images[0].save(img_paths[i], 'JPEG')