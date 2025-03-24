using GFN_IoT_Project.Components;
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

            // add MudBlazor services
            builder.Services.AddMudServices();
            //add custom classes
            builder.Services.AddSingleton<ApiDataList>();
            builder.Services.AddSingleton<GetDataList>();
            builder.Services.AddSingleton<GFNLogger>();
            builder.Services.AddSingleton<DatabaseManager>();
           
            // add services to the container.
            builder.Services.AddRazorComponents()
                .AddInteractiveServerComponents();
            //add api controles
            builder.Services.AddControllers();
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

            app.UseAntiforgery();

            app.MapStaticAssets();
            app.MapRazorComponents<App>()
                .AddInteractiveServerRenderMode();

            app.Run();
        }
    }
}
