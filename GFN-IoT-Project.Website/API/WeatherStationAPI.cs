using GFN_IoT_Project.Extensions;
using GFN_IoT_Project.Extensions.Database;
using GFN_IoT_Project.Extensions.Logger;
using GFN_IoT_Project.Lists;
using Microsoft.AspNetCore.Mvc;

namespace GFN_IoT_Project.API
{
    [Route("[controller]")]
    [ApiController]
    public class WeatherStationAPIController : ControllerBase
    {
        // Database and SQL query managers
        private readonly DatabaseManager CONN;
        private readonly SqlQueryManager SQL;

        //constructor
        public WeatherStationAPIController(DatabaseManager db, SqlQueryManager sql)
        {
            CONN = db;
            SQL = sql;
        }
        // Endpoint to post the temp sensor data
        [HttpPost("SendTempData")]
        public async Task<IActionResult> SendTempData([FromBody] ApiDataList Data, [FromHeader] string? APIKey, [FromServices] LiveUpdateService liveUpdateService)
        {
            try
            {
                // Check if the API key is valid
                var apiKey = await CONN.LoadDataType<bool, dynamic>(SQL.GET_API_KEY, new { APIKey });
                // If the API key is invalid, return a 403 Forbidden status code
                if (!apiKey)
                {
                    GFNLogger.Log("Unauthorized API access attempt.");
                    return StatusCode(403, "Invalid API Key.");
                }
                // If the API key is valid, update the temp sensor data
                liveUpdateService.UpdateTemp = Data.DataValue;

                // If the API key is valid, insert the data into the database
                await CONN.InsertData<dynamic>(SQL.INSERT_TEMPERATURE_DATA, new
                {
                    Temp = Data.DataValue,
                });
                // Return a 200 OK status code
                return StatusCode(200);
            }
            catch (Exception ex)
            {
                // Log the error message
                GFNLogger.Log($"Error: {ex.Message}");
                return StatusCode(500, $"Error: {ex.Message}");
            }
        }
    }
}
