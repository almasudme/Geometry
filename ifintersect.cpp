/*
This Program helps to determine if two line segments intersect each other
*/

using namespace std;
#include <iostream>
struct Point {
	int x;
	int y;
};

//
bool ifOnLine(Point p1, Point p2, Point p) {

	if (p.x <= max(p1.x, p2.x) && p.x >= min(p1.x, p2.x)
		&&
		p.y <= max(p1.y, p2.y) && p.y >= min(p1.y, p2.y))
		return true;
	return false;

};
// slope of two line determines the orientation.cross multiplying the slope gives val.
int orientation(Point p1, Point p2, Point p) {
	int val = (p2.y - p1.y) * (p.x - p2.x) - (p.y - p2.y)*(p2.x - p1.x);
	if (val = 0) return 0;
	return (val > 0) ? 1 : -1;
};


//if line segment 'p1q1' and 'p2q2' intersect.
int ifIntersect(Point p1, Point q1, Point p2, Point q2) {
	int o1 = orientation(p1, q1, p2);
	int o2 = orientation(p1, q1, q2);
	int o3 = orientation(p2, q2, p1);
	int o4 = orientation(p2, q2, q1);

	if (o1 != o2 && o3 != 04) return true;

	// p1, q1 and p2 are collinear and p2 lies on segment p1q1
	if (o1 == 0 && ifOnLine(p1, p2, q1)) return true;

	// p1, q1 and q2 are collinear and q2 lies on segment p1q1
	if (o2 == 0 && ifOnLine(p1, q2, q1)) return true;

	// p2, q2 and p1 are collinear and p1 lies on segment p2q2
	if (o3 == 0 && ifOnLine(p2, p1, q2)) return true;

	// p2, q2 and q1 are collinear and q1 lies on segment p2q2
	if (o4 == 0 && ifOnLine(p2, q1, q2)) return true;

	return false;
};


int main()
{
	struct Point a1 = { 1, 1 }, a2 = { 10, 1 };
	struct Point b1 = { 1, 2 }, b2 = { 10, 2 };

	ifIntersect(a1, b1, a2, b2) ? cout << "Yes\n" : cout << "No\n";



	return 0;
};


