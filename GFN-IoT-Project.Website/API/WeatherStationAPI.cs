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
        //create a new database manager
        DatabaseManager dbMen = new();
        // Endpoint to post the temp sensor data
        [HttpPost("SendTempData")]
        public IActionResult SendTempData ([FromBody] ApiDataList request)
        {
            try
            {
                //dbMen.SaveData<dynamic>();
                return StatusCode(200);
            }
            catch (UnauthorizedAccessException ex)
            {
                GFNLogger.Log($"Access denied: {ex.Message}");
                return StatusCode(403, $"Access denied: {ex.Message}");
            }
            catch (Exception ex)
            {
                GFNLogger.Log($"Error: {ex.Message}");
                return StatusCode(500, $"Error: {ex.Message}");
            }
        }
    }
}
