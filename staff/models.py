from django.db import models
from django.urls import reverse


class StaffMember(models.Model):
    class Role(models.TextChoices):
        BARBER = "barber", "Barber"
        HAIRDRESSER = "hairdresser", "Hairdresser"
        TATTOO_ARTIST = "tattoo_artist", "Tattoo Artist"
        ESTHETICIAN = "esthetician", "Esthetician"

    name = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=Role.choices)
    bio = models.TextField(blank=True, help_text="Short bio shown on the artist's profile page.")
    cover_photo = models.ImageField(
        upload_to="staff/covers/",
        help_text="Main photo shown on the artist card.",
    )
    instagram_link = models.URLField(
        blank=True, help_text="Full Instagram profile or post URL (optional)."
    )
    is_active = models.BooleanField(
        default=True, help_text="Uncheck to hide this artist from the site without deleting them."
    )
    order = models.PositiveIntegerField(
        default=0, help_text="Lower numbers appear first."
    )

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return f"{self.name} ({self.get_role_display()})"

    def get_absolute_url(self):
        return reverse("staff:detail", kwargs={"pk": self.pk})


class StaffPhoto(models.Model):
    staff = models.ForeignKey(StaffMember, related_name="photos", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="staff/photos/")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"Photo for {self.staff.name} (#{self.order})"


class StaffVideo(models.Model):
    staff = models.ForeignKey(StaffMember, related_name="videos", on_delete=models.CASCADE)
    video_file = models.FileField(
        upload_to="staff/videos/",
        blank=True,
        help_text="Upload a video file directly (keep clips short/compressed).",
    )
    video_url = models.URLField(
        blank=True,
        help_text="Or paste an Instagram reel / YouTube link instead of uploading a file.",
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"Video for {self.staff.name} (#{self.order})"