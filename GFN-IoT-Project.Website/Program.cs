using GFN_IoT_Project.Components;
using GFN_IoT_Project.Extensions;
using GFN_IoT_Project.Extensions.Database;
using GFN_IoT_Project.Extensions.Logger;
using GFN_IoT_Project.Lists;
using MudBlazor.Services;
using SQLitePCL;

namespace GFN_IoT_Project
{
    public class Program
    {
        public static void Main(string[] args)
        {
            //craete the databse if not exists 
            Batteries.Init();
            DatabaseManager.CreateDatabase();

            var builder = WebApplication.CreateBuilder(args);
            //add swagger
            builder.Services.AddSwaggerGen();
            // add MudBlazor services
            builder.Services.AddMudServices();
            //add custom classes
            builder.Services.AddSingleton<GetDataList.TemperatureData>();
            builder.Services.AddSingleton<GFNLogger>();
            builder.Services.AddSingleton<DatabaseManager>();
            builder.Services.AddSingleton<SqlQueryManager>();
            builder.Services.AddSingleton<LiveUpdateService>();

            // add services to the container.
            builder.Services.AddRazorComponents()
                .AddInteractiveServerComponents();
            //add api controles
            builder.Services.AddControllers();
            builder.Services.AddEndpointsApiExplorer();
            //add swager
            builder.Services.AddSwaggerGen();
            var app = builder.Build();

            // Configure the HTTP request pipeline.
            if (!app.Environment.IsDevelopment())
            {
                app.UseExceptionHandler("/Error");
                // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
                app.UseHsts();
            }
            //use swagger
            app.UseSwagger();
            app.UseSwaggerUI();
            app.UseHttpsRedirection();
            app.UseRouting();

            app.UseAntiforgery();

            app.MapControllers();
            app.MapStaticAssets();
            app.MapRazorComponents<App>()
                .AddInteractiveServerRenderMode();

            app.Run();
        }
    }
}
