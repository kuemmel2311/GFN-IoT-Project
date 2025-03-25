namespace GFN_IoT_Project.Extensions.Database
{
    public class SqlQueryManager
    {
        public string GET_TEMPERATURE_DATA = "SELECT * FROM temperature_data WHERE timestamp BETWEEN @StartTime and @NowTime";
        public string GET_HUMIDITY_DATA = "SELECT * FROM humidity_data WHERE timestamp BETWEEN @StartTime and @NowTime";
        public string GET_PRESSURE_DATA = "SELECT * FROM pressure_data WHERE timestamp BETWEEN @StartTime and @NowTime";
        public string GET_AIR_QUALITY_DATA = "SELECT * FROM air_quality_data WHERE timestamp BETWEEN @StartTime and @NowTime";
        public string GET_API_KEY = "SELECT * FROM api_keys WHERE key = @APIKey";
        public string INSERT_TEMPERATURE_DATA = "INSERT INTO temperature_data (temperature) VALUES (@Temp);";
        public string INSERT_HUMIDITY_DATA = "INSERT INTO humidity_data (humidity) VALUES (@Humidity);";
        public string INSERT_PRESSURE_DATA = "INSERT INTO pressure_data (pressure) VALUES (@Pressure);";
        public string INSERT_AIR_QUALITY_DATA = "INSERT INTO air_quality_data (air_quality) VALUES (@AirQ);";
    }
}
