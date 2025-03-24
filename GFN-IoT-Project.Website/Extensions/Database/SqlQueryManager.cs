namespace GFN_IoT_Project.Extensions.Database
{
    public class SqlQueryManager
    {
        public static string GET_TEMPERATURE_DATA = "SELECT * FROM temperature_data WHERE timestamp BETWEEN @StartTime and @NowTime";
        public static string GET_HUMIDITY_DATA = "SELECT * FROM humidity_data WHERE timestamp BETWEEN @StartTime and @NowTime";
        public static string GET_PRESSURE_DATA = "SELECT * FROM pressure_data WHERE timestamp BETWEEN @StartTime and @NowTime";
        public static string GET_AIR_QUALITY_DATA = "SELECT * FROM air_quality_data WHERE timestamp BETWEEN @StartTime and @NowTime";
    }
}
