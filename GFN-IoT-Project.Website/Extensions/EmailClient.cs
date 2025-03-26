namespace GFN_IoT_Project.Extensions
{
    using System;
    using System.Net;
    using System.Net.Mail;
    public class EmailClient 
    {
        private readonly string _smtpServer = "smtp.gmail.com";
        private readonly int _port = 587; // TLS-port für Gmail
        private readonly string _emailUsername = Environment.GetEnvironmentVariable("EMAIL_USER")
            ?? throw new ArgumentNullException(nameof(_emailUsername), "Die Umgebungsvariable 'EMAIL_USER' ist nicht gesetzt.");
        private readonly string _emailPassword = Environment.GetEnvironmentVariable("EMAIL_pass")
            ?? throw new ArgumentNullException(nameof(_emailPassword), "Die Umgebungsvariable 'EMAIL_PASS' ist nicht gesetzt.");



        public void SendEmial(string from, string to, string subject, string body) 
        {
            try
            {
                using (MailMessage mail = new MailMessage())
                {
                    mail.From = new MailAddress(from);
                    mail.To.Add(to);
                    mail.Subject = subject;
                    mail.Body = body;
                    mail.IsBodyHtml = false; // Falls HTM erlaubt ist, auf true setzen

                    using (SmtpClient smtp = new SmtpClient(_smtpServer, _port))
                    {
                        smtp.Credentials = new NetworkCredential(_emailUsername, _emailPassword);
                        smtp.EnableSsl = true;
                        smtp.DeliveryMethod = SmtpDeliveryMethod.Network;
                        smtp.Send(mail);
                    }

                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Fehler beim Senden der E-Mail: {ex.Message}");

            }
        }



    }

}
