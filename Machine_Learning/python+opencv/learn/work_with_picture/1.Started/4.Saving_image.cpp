// c++ code explaining how to
// save an image to a defined
// location in OpenCV

// loading library files
#include <highlevelmonitorconfigurationapi.h>
#include <opencv2\highgui\highgui.hpp>
#include <opencv2\opencv.hpp>

using namespace cv;
using namespace std;

int main(int argc, char** argv)
{

    // Reading the image file from a given location in system
    Mat img = imread("..path\\abcd.jpg");

    // if there is no image
    // or in case of error
    if (img.empty()) {
        cout << "Can not open or image is not present" << endl;

        // wait for any key to be pressed
        cin.get();
        return -1;
    }

    // You can make any changes
    // like blurring, transformation

    // writing the image to a defined location as JPEG
    bool check = imwrite("..path\\MyImage.jpg", img);

    // if the image is not saved
    if (check == false) {
        cout << "Mission - Saving the image, FAILED" << endl;

        // wait for any key to be pressed
        cin.get();
        return -1;
    }

    cout << "Successfully saved the image. " << endl;

    // Naming the window
    String geek_window = "MY SAVED IMAGE";

    // Creating a window
    namedWindow(geek_window);

    // Showing the image in the defined window
    imshow(geek_window, img);

    // waiting for any key to be pressed
    waitKey(0);

    // destroying the creating window
    destroyWindow(geek_window);

    return 0;
}
