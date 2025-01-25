#include <bits/stdc++.h>
#include <SFML/Graphics.hpp>
using namespace std;
int main()
{
    ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    vector<float> x_values;
    vector<float> y_values;

    for (float x = -5.0f; x <= 5.0f; x += 0.1f) {
        x_values.push_back(x);
        y_values.push_back(sin(x)); // Example: sin(x) function
    }

    // Create the window
    RenderWindow window(VideoMode(800, 600), "Simple Plot");

    // Define the plot area
    float plot_width = 600.0f;
    float plot_height = 400.0f;
    float x_offset = 50.0f;
    float y_offset = 50.0f;

    // Find the minimum and maximum values for scaling
    float min_x = *min_element(x_values.begin(), x_values.end());
    float max_x = *max_element(x_values.begin(), x_values.end());
    float min_y = *min_element(y_values.begin(), y_values.end());
    float max_y = *max_element(y_values.begin(), y_values.end());

    // Create a scaling function
    auto scale_x = [&](float x) {
        return x_offset + (x - min_x) / (max_x - min_x) * plot_width;
    };
    auto scale_y = [&](float y) {
        return y_offset + (1.0f - (y - min_y) / (max_y - min_y)) * plot_height; 
    };

    // Create a line shape
    VertexArray line(LinesStrip, x_values.size());
    for (size_t i = 0; i < x_values.size(); ++i) {
        line[i].position = Vector2f(scale_x(x_values[i]), scale_y(y_values[i]));
    }

    // Create axes
    VertexArray x_axis(Lines, 2);
    x_axis[0].position = Vector2f(x_offset, y_offset);
    x_axis[1].position = Vector2f(x_offset + plot_width, y_offset);

    VertexArray y_axis(Lines, 2);
    y_axis[0].position = Vector2f(x_offset, y_offset);
    y_axis[1].position = Vector2f(x_offset, y_offset + plot_height);

    // Run the game loop
    while (window.isOpen())
    {
        Event event;
        while (window.pollEvent(event))
        {
            if (event.type == Event::Closed)
                window.close();
        }

        window.clear(Color::Black);
        window.draw(x_axis);
        window.draw(y_axis);
        window.draw(line);
        window.display();
    }

    return 0;
}