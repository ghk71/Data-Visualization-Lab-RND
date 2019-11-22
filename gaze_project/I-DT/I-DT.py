#I-VT & I-DT clustering algoritm: reference https://github.com/ecekt/eyegaze.git
#ece k.t.
from __future__ import division
import numpy as np
from collections import Counter

#column indices of attributes, check csv file
index = 0
timestamp = 1
question = 2
x = 3
y = 4
user_id = 5
group_size = 6
gaze_cue = 7

def idt(data, dis_threshold, dur_threshold):
  window_range = [0,0]
	current = 0 #pointer to represent the current beginning point of the window
	last = 0
  
	#final lists for fixation info
	centroidsX = []
	centroidsY = []
	time0 = []
	time1 = []
	
	while (current < len(data)):
        
		t0 = float(data[current][timestamp]) #beginning time
		t1 = t0 + float(dur_threshold)     #time after a min. fix. threshold has been observed

		for r in range(current, len(data)): 
			if(float(data[r][timestamp])>= t0 and float(data[r][timestamp])<= t1):
				#print "if",r
				last = r #this will find the last index still in the duration threshold

		window_range = [current,last]
		
		#now check the dispersion in this window
		#print "window", current, last
		dispersion = get_dispersion(data[current:last+1])
		#a[2:5] gives 2,3,4. To include last one, [2:6]

	
	
def get_dispersion(points):
	dispersion = 0
    	argxmin = np.min(points[:,x].astype(np.float))
	argxmax = np.max(points[:,x].astype(np.float))
    	argymin = np.min(points[:,y].astype(np.float))
	argymax = np.max(points[:,y].astype(np.float))
	
	dispersion = ((argxmax - argxmin) + (argymax - argymin))/2
	#TODO: look for other ways of calculating dispersion
	
	return dispersion
