import matplotlib.pyplot as plt


class TemperatureAnalytics:

  def __init__(self, data):
    self.data = data

  def get_average_temperature(self, year):
    yearly_data = self.data[self.data['rok'] == year]
    return yearly_data['T-AVG'].mean()

  def get_max_temperature(self, year):
    yearly_data = self.data[self.data['rok'] == year]
    max_temp = yearly_data['TMA'].max()
    date_of_max_temp = yearly_data[yearly_data['TMA'] == max_temp][[
        'rok', 'měsíc', 'den'
    ]].iloc[0]
    return max_temp, date_of_max_temp

  def get_min_temperature(self, year):
    yearly_data = self.data[self.data['rok'] == year]
    min_temp = yearly_data['TMI'].min()
    date_of_min_temp = yearly_data[yearly_data['TMI'] == min_temp][[
        'rok', 'měsíc', 'den'
    ]].iloc[0]
    return min_temp, date_of_min_temp

  def get_min_temp_day(self, day):
    day_data = self.data[self.data['den'] == day]
    min_temp = day_data['TMI'].min()
    date_of_min_temp = day_data[day_data['TMI'] == min_temp][[
        'rok', 'měsíc', 'den'
    ]].iloc[0]
    return min_temp, date_of_min_temp

  def get_max_temp_day(self, day):
    day_data = self.data[self.data['den'] == day]
    max_temp = day_data['TMI'].max()
    date_of_max_temp = day_data[day_data['TMI'] == max_temp][[
        'rok', 'měsíc', 'den'
    ]].iloc[0]
    return max_temp, date_of_max_temp

  def get_monthly_averages(self, year):
    yearly_data = self.data[self.data['rok'] == year]
    return yearly_data.groupby('měsíc')['T-AVG'].mean()

  def analyze_temperature_trends(self, start_year, end_year):
    trend_data = self.data[(self.data['rok'] >= start_year)
                           & (self.data['rok'] <= end_year)]
    annual_average_temperatures = trend_data.groupby('rok')['T-AVG'].mean()
    plt.figure(figsize=(10, 6))
    plt.plot(annual_average_temperatures.index,
             annual_average_temperatures.values,
             marker='o',
             linestyle='-',
             color='b')
    plt.title('Trendy teplot')
    plt.xlabel('Rok')
    plt.ylabel('Teplota (°C)')
    plt.grid(True)
    plt.show()

  def plot_annual_temperature_averages(self, start_year, end_year):
    filtered_data = self.data[(self.data['rok'] >= start_year)
                              & (self.data['rok'] <= end_year)]
    annual_average_temps = filtered_data.groupby('rok')['T-AVG'].mean()
    plt.figure(figsize=(10, 6))
    plt.plot(annual_average_temps.index,
             annual_average_temps.values,
             marker='o',
             linestyle='-',
             color='b')
    plt.title('Růst teplot v roce')
    plt.xlabel('Rok')
    plt.ylabel('Teplota (°C)')
    plt.grid(True)
    plt.show()

  def menu(self):
    print("1 - Zobrazit průměrnou teplotu pro zadaný rok")
    print("2 - Zobrazit minimální a maximální teplotu pro zadaný rok")
    print("3 - Zobrazit měsíční průměry pro zadaný rok")
    print("4 - Vykreslit průměrné roční teploty")
    print("5 - Vykreslit trendy")
    print("6 - Vykreslit teplotu za den")
    print("0 - Konec")
    volba = input("Zvolte možnost: ")
    return volba

  def plot_daily_temperature(self, day, month, year):
    day_data = self.data[(self.data['den'] == day)
                         & (self.data['měsíc'] == month) &
                         (self.data['rok'] == year)]
    min = day_data['TMI'].min()
    max = day_data['TMI'].max()
    return min, max
