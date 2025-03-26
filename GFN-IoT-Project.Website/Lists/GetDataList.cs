using Microsoft.VisualBasic;

namespace GFN_IoT_Project.Lists
{
    public class GetDataList
    {
        public class TemperatureData
        {
            public int Id { get; set; }
            public DateTime? Timestamp { get; set; }
            public double? Temperature { get; set; }
        }

        public class HumidityData
        {
            public int Id { get; set; }
            public DateTime Timestamp { get; set; }
            public double Humidity { get; set; }
        }

        public class PressureData
        {
            public int Id { get; set; }
            public DateTime Timestamp { get; set; }
            public double Pressure { get; set; }
        }

        public class AirQualityData
        {
            public int Id { get; set; }
            public DateTime Timestamp { get; set; }
            public double AirQuality { get; set; }
        }

        public class LightLevelData
        {
            public int Id { get; set; }
            public DateTime Timestamp { get; set; }
            public double LightLevel { get; set; }
        }

        public class ApiKey
        {
            public int Id { get; set; }
            public string Key { get; set; }
            public string Owner { get; set; }
            public DateTime CreatedAt { get; set; }
        }
    }
}
