namespace GFN_IoT_Project.Extensions
{
    public class LiveUpdateService
    {
        public event Action? OnTemperatureUpdate;
        private double _latestTemperature = 0.0;

        public double UpdateTemp
        {
            get => _latestTemperature;
            set
            {
                _latestTemperature = value;
                OnTemperatureUpdate?.Invoke();
            }
        }
    }
}
