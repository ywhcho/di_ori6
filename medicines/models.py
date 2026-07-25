from django.db import models


class Medicine(models.Model):
    """의약품 모델 (약품명, 성분명, 회사명, 주성분코드)"""
    htname = models.CharField(max_length=200, verbose_name='약품명')
    ingr_t = models.CharField(max_length=1000, verbose_name='성분명')
    e2iact_t = models.CharField(max_length=1000, verbose_name='성분함량')
    ee = models.TextField(blank=True, verbose_name='효능')
    company = models.CharField(max_length=200, verbose_name='회사명')
    wfco = models.CharField(max_length=10, blank=True, default='', db_index=True, verbose_name='주성분코드')

    class Meta:
        verbose_name = '의약품'
        verbose_name_plural = '의약품 목록'
        ordering = ['htname']

    def __str__(self):
        return self.htname


class DrugInfo(models.Model):
    """의약정보 상세 모델 (htname, ingr_t, ee, ud_html, nb_html, company, ypri24, kfregcd, canc_date)"""
    kfregcd = models.CharField(max_length=50, blank=True, default='', verbose_name='품목기준코드')
    canc_date = models.CharField(max_length=20, blank=True, default='', verbose_name='사용종료일')
    htname = models.CharField(max_length=200, verbose_name='약품명')
    ingr_t = models.CharField(max_length=1000, verbose_name='성분명')
    company = models.CharField(max_length=200, verbose_name='회사명')
    ypri24 = models.BigIntegerField(null=True, blank=True, verbose_name='연생산액')
    ee = models.TextField(blank=True, verbose_name='효능')
    ud_html = models.TextField(blank=True, db_column='ud', verbose_name='용량')
    nb_html = models.TextField(blank=True, db_column='nb', verbose_name='주의사항')

    class Meta:
        verbose_name = '의약정보'
        verbose_name_plural = '의약정보 목록'
        ordering = ['htname']

    def __str__(self):
        return self.htname
