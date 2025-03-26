namespace GFN_IoT_Project.Extensions
{
    using System.Linq.Expressions;
    using System.Net;
    using System.Net.Mail;
    using System.Reflection.Metadata.Ecma335;

    public class EmailClient {
        public void SendEmail(string from, string to, string subject, string body)
        {
            MailMessage mail = new MailMessage(from, to);
            mail.Subject = subject;
            mail.Body = body;
            SmtpClient smtp = new SmtpClient("smtp.gmail.com");
            smtp.Credentials = new NetworkCredential("ypor-email", "your-password");
            smtp.EnableSsl = true;
            smtp.Send(mail);
        }



        public void Connect(string server, string username, string password)
        {
            try
            {
                if (_isConnected)
                {
                    return;
                }
                if (!UseSSL)
                {
                    connect(server, PortNumber);
                    string response = response();
                    if (response.Trim().StartsWith("+OK"))
                    {
                        //TODO: Raise Error  Event
                    }
                    else
                    {
                        ExecuteCommand("User", username);
                        ExecuteCommand("Pass", password);

                    }
                    _isConnected = true;
                }
                else
                {
                    //SSL-Verbindung mit Authentifizierung
                }
            }


            Catch (Exception ex)
            {
                //TODO: Raise Error Event
            }

        }
    }

}
