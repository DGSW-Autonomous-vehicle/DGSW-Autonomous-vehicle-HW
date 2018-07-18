#ifndef __OBSTACLE_H__
#define __OBSTACLE_H__

#define OBS_DEBUG 0
#define OBS_RELEASE 1

#include <opencv2/opencv.hpp> 
#include <vector>
#include <cmath>

using namespace cv;

class OpenCV_OBS {
private:
	Mat image;
	Rect road;

public:
	OpenCV_OBS();

	void setResources(Mat img, Rect areaOfRoad);
	bool hasOBS(Size minSize, int flag);
};

#endif
