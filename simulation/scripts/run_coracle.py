#!/usr/bin/env python

"""Runs the Coracle simulator using the configuration file
generated by sim_config_json.py and visualizes the result as a PDF report
"""

import os
import sys
import json
import subprocess
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages


class Visualizer():

    def __init__(self):
        self.tables = []
        self.figures = []

    def parse(self, results):
        for key,value in results.items():

            if (key == "table"):
                self.tables.append(value)

            elif (key == "figures"):
                self.figures.append(value)

            if type(value) is dict:
                self.parse(value)
    
    def build_figure(self, fig, ax, raw_figure):

        ax.set(xlabel=raw_figure['x axis']['label'], 
               xlim=(raw_figure['x axis']['start'], raw_figure['x axis']['end']), 
               ylabel=raw_figure['y axis']['label'], 
               ylim=(raw_figure['y axis']['start'], raw_figure['y axis']['end']), 
               title=raw_figure['title'])
        
        for line in raw_figure['data']:
            x_points = []
            y_points = []
            for data_point in line['data']:
                x_points.append(data_point['x'])
                y_points.append(data_point['y'])
            ax.plot(x_points, y_points)

    def generate_pdf(self):
        
        with PdfPages("./test.pdf") as export_pdf:
            for table in self.tables:
                df = pd.DataFrame.from_dict(table, orient='index')
                fig, ax = plt.subplots(figsize=(10, 6))
                plt.axis('off')
                pd.plotting.table(ax, df, loc='center')
                fig.tight_layout()
                export_pdf.savefig()
                plt.close()  

            for raw_figure_set in self.figures:
                if raw_figure_set:
                    for raw_figure in raw_figure_set:
                        fig, ax = plt.subplots(figsize=(10, 6))
                        self.build_figure(fig, ax, raw_figure)
                        export_pdf.savefig()
                        plt.close()
                        
def main(arguments):

    opam_eval = 'eval `opam config env --safe`'
    val = subprocess.check_output("%s && ./../coracle/coracle_sim.byte %s %s" % (opam_eval, "-f", "test.json"), shell=True)
    raw_out = json.loads(val)
    raw_res = raw_out['results']

    visualizer = Visualizer()
    visualizer.parse(raw_res)
    visualizer.generate_pdf()

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
