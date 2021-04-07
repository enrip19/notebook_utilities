import os
import csv
import glob
import numpy as np

class csv_file:
    def __init__(self,path,date,headers='time(s),current(A)'):
        self.path = path
        self.date = date
        self.filepath = path + date
        self.headers = headers

        self.csvfiles = glob.glob(os.path.join(self.filepath, '*.csv'))
        self.data = list(np.zeros(len(self.csvfiles)))
        self.filenames = list(np.zeros(len(self.csvfiles)))
        self.headers = []
        self.units = []

    def read_csvFiles(self):
        for file in self.csvfiles:
            with open(file, 'r') as f:
                csv_file = csv.reader(f,delimiter=',')
                self.headers.append(next(csv_file))
                self.data[self.csvfiles.index(file)] = np.array(list(csv_file))
            f.close()
            self.filenames[self.csvfiles.index(file)] = os.path.splitext(os.path.basename(file))[0]        
        return self.filenames,self.headers,self.data

    def extract_data(self):
        for k in range(len(self.filenames)):
            for i in self.headers:
                globals()[f'index{i}_Header'] = self.headers[k].index(self.headers[0][0])
            
            globals()[f'{self.headers[k]}'] = np.asarray(self.data[k][:,globals()[f'index{i}_Header']],dtype='float64')
            return globals()[f'{self.headers[k]}']
   
    
    def plotFoxes(x,y,title,xlabel, ylabel,pngName,pngPath,legend=True,save=True):
        fig1, ax1 = plt.subplots()
        line1 = ax1.plot(x, y, color=foxes_rgb, label=ylabel[:-4]  )
        # print(seconds[1]-seconds[0])
        xmin = min(x)
        xmax = max(x)
        ymin = min(y)
        ymax = max(y)

        avg = 0
        avg = np.average(y)
        print('Average: ',avg)
        ax1.set_xlim(xmin-0.05,xmax+0.05)

        pngName = pngName
        path = pngPath  + '\\images'+ '\\' + date

        #lines:
        #fig1.vlines(50,ymin,ymax,colors='')
        line2 = ax1.axhline(avg, color=darkFoxes_rgb, label='average')

        #format:
        fig1.set_facecolor('white')
        

        ax1.set_title(title, pad=3.5, fontweight='bold')#, y=1.1)
        ax1.set_xlabel(xlabel,ha='center',fontweight='bold')
        ax1.set_ylabel(ylabel,va='center',fontweight='bold')
        
        ax1.yaxis.set_minor_locator(AutoMinorLocator())
        ax1.xaxis.set_minor_locator(AutoMinorLocator())
        ax1.tick_params(which='minor',length=4, color='k')
        ax1.grid()
        #ax1.label_outer()
        #legend:
        lines, labels = ax1.get_legend_handles_labels()
        if(legend==True):
            ax1.legend(lines,labels,loc='upper right')
        #ax1.set(xlim=(min(date),max(date)),ylim=(min(RSSI),max(RSSI)))
        
        if(save==True): 
            try:
                os.mkdir(path)
            except:
                print('The directory exists. Image saved.')
            else:        
                print('Directory images has created. Image saved.')    
            
            fig1.savefig(path + '\\' +  pngName + '.png', format='png', dpi=800, bbox_inches='tight')

        plt.show()
    
   

            

