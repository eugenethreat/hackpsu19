# hackpsu19

RUN GUI



Inspiration

After hearing about the GEICO Challenge to implement weather data in a way that can help consumers, we thought, "What's one thing we always hear about from insurance companies on TV?" -- Driving Safer. Thinking back to times we've all had to drive under unsafe conditions, we figured if we could implement weather data into a user's route, we could help them to drive safer AND save money on their car insurance.
What it does and how we built it

Our app allows the user to input a starting and ending location, and then utilizing the Google Maps API, it calculated the latitudes and longitudes of the beginning, end, and crucial points throughout the most optimal route. Pushing that data into the AccuWeather API then allows us to find a 12-hour forecast for the data. By comparing the weather data based on different times of the day in different positions, we can calculate when it would be best for the user to leave their home to head on their trip. Then we tell the user whether or not they should delay their trip, and by how long they should.
Challenges we ran into

The Google Maps API proved to be a significantly bigger challenge to parse than we intended. The raw amount of data that would get pushed with a single API call required us to implement some heavy filtration in order to retrieve and appropriately deliver the information we needed for the rest of the program to run.
Accomplishments that we're proud of:
What we learned:

With this being 2/3 of our group's first time delving into APIs and Github, we learned both how to accurately use and parse data from APIs as well as how to work together better utilizing Github to work individually while contributing to the overall project nearly instantaneously. Additionally, we learned how to parse large JSON files to be usable through python code through the use of the Google Maps API.
What's next for Let's Take A Trip:

Let's Take A Trip has the potential to become both a powerhouse in travel as well as a way to help people travel safer as well as plan their trips to avoid hazards that could potentially delay their trip massively. The next step for Let's Take a Trip is to further develop the predictive weather technology by adding more points along our route, allowing the weather to be displayed even more accurately to the user.

By improving the ability to better improve people's travel in day-to-day life -- we would be able to draw more people to the Geico site. We would want to also push some information to the user that could persuade them to make the switch to Geico or upgrade their current plan. This information could include: Showing how much the potential weather could've cost them to repair, or by showing users the fuel saved by avoiding stop-and-go weather traffic.

The other path would be to better it as a stand-alone travel companion, we would like to utilize popular websites such as Trivago or Hotels.com to allow users to be able to adjust not only their route but allow them to schedule future portions of their trip/hotel accommodations all in one place.
