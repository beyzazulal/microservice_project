using System.Text;
using System.Text.Json;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

// Diğer servisler buraya bildirim mesajı gönderecek
app.MapPost("/api/notify", async (NotificationRequest req) =>
{
    var slackUrl = "https://hooks.slack.com/services/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";
    
    var payload = new { text = $"📢 *Sistem Bildirimi:*\n{req.Message}" };
    
    using var client = new HttpClient();
    var content = new StringContent(JsonSerializer.Serialize(payload), Encoding.UTF8, "application/json");
    
    var response = await client.PostAsync(slackUrl, content);

    if (response.IsSuccessStatusCode)
        return Results.Ok("Bildirim Slack'e gönderildi.");
    
    return Results.Problem("Slack bağlantı hatası!");
});

app.Run();

// Beklediğimiz veri yapısı
record NotificationRequest(string Message);