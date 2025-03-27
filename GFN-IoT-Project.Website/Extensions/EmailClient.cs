using System.Net;
using System.Net.Mail;
using GFN_IoT_Project.Extensions.Logger;
using static System.Collections.Specialized.BitVector32;

namespace GFN_IoT_Project.Extensions
{
    public class EmailClient
    {
        private readonly string _smtpServer;
        private readonly int _smtpPort;
        private readonly string _senderEmail;
        private readonly string _senderPassword;
        private readonly string _recipientEmail;

        public EmailClient(string smtpServer, int smtpPort, string senderEmail,
                           string senderPassword, string recipientEmail)
        {
            _smtpServer = smtpServer;
            _smtpPort = smtpPort;
            _senderEmail = senderEmail;
            _senderPassword = senderPassword;
            _recipientEmail = recipientEmail;
        }

        public async Task SendEmailAsync(string subject, string body)
        {
            await SendAsync(subject, body);
        }

        private async Task SendAsync(string subject, string body)
        {
            try
            {
                using var smtpClient = new SmtpClient(_smtpServer)
                {
                    Port = _smtpPort,
                    Credentials = new NetworkCredential(_senderEmail, _senderPassword),
                    EnableSsl = true,
                };

                using var mailMessage = new MailMessage
                {
                    From = new MailAddress(_senderEmail, "Smart Weather Station"),
                    Subject = subject,
                    Body = body,
                    IsBodyHtml = false,
                };
                mailMessage.To.Add(_recipientEmail);

                await smtpClient.SendMailAsync(mailMessage);
                GFNLogger.Log("E-Mail erfolgreich gesendet!");
            }
            catch (Exception ex)
            {
                GFNLogger.Log($"Fehler beim Senden der E-Mail: {ex.Message}");
            }
        }
    }
}
