import cv2
import numpy as np

A = cv2.imread('spheroids_Snapshot_20240406_01_rgb.ome');
cv2.imshow(A)
Rmin = 50;
Rmax = 800;
[centersBright, radiiBright] = cv2.imfindcircles(A,[Rmin Rmax],'ObjectPolarity','bright');
[centersDark, radiiDark] = cv2.imfindcircles(A,[Rmin Rmax],'ObjectPolarity','dark');
cv2.viscircles(centersBright, radiiBright,'Color','b');
