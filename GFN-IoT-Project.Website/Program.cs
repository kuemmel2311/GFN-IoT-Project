using GFN_IoT_Project.Components;
using GFN_IoT_Project.Extensions.Database;
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

            // Add MudBlazor services
            builder.Services.AddMudServices();

            // Add services to the container.
            builder.Services.AddRazorComponents()
                .AddInteractiveServerComponents();

            var app = builder.Build();

            // Configure the HTTP request pipeline.
            if (!app.Environment.IsDevelopment())
            {
                app.UseExceptionHandler("/Error");
                // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
                app.UseHsts();
            }

            app.UseHttpsRedirection();

            app.UseAntiforgery();

            app.MapStaticAssets();
            app.MapRazorComponents<App>()
                .AddInteractiveServerRenderMode();

            app.Run();
        }
    }
}
