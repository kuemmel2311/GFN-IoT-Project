namespace GFN_IoT_Project.Extensions
{
    public class LiveUpdateService
    {
        // Event handlers for updating the UI
        public event Action? OnTemperatureUpdate;
        public event Action? OnHumidityUpdate;
        public event Action? OnPressureUpdate;
        public event Action? OnAirQualityUpdate;
        public event Action? OnDayNightUpdate;

        // Latest sensor data values
        private double _latestTemperature = 0.0;
        private double _latestHumidity = 0.0;
        private int _latestPressure = 0;
        private double _latestAirQuality = 0.0;
        private int _latestDayNight = 0;    

        // Properties to update the sensor data values
        public double UpdateTemp
        {
            get => _latestTemperature;
            set
            {
                _latestTemperature = value;
                OnTemperatureUpdate?.Invoke();
            }
        }
        public double UpdateHumidity
        {
            get => _latestHumidity;
            set
            {
                _latestHumidity = value;
                OnHumidityUpdate?.Invoke();
            }
        }
        public int UpdatePressure 
        {
            get => _latestPressure;
            set
            {
                _latestPressure = value;
                OnPressureUpdate?.Invoke();
            }
        }
        public double UpdateAirQuality
        {
            get => _latestAirQuality;
            set
            {
                _latestAirQuality = value;
                OnAirQualityUpdate?.Invoke();
            }
        }
        public int UpdateDayNight
        {
            get => _latestDayNight;
            set
            {
                _latestDayNight = value;
                OnDayNightUpdate?.Invoke();
            }
        }
    }
}
