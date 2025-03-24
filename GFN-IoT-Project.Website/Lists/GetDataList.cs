using Microsoft.VisualBasic;

namespace GFN_IoT_Project.Lists
{
    public class GetDataList
    {
        public int ID { get; set; }
        public required DateAndTime DateAndTime { get; set; }
        public required int DataValue {  get; set; } 
    }
}
