from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.


# class prefecture(models.Model):
#     """都道府県テーブル"""

#     prefID = models.IntegerField(verbose_name='都道府県ID')
#     prefname = models.CharField(verbose_name='都道府県名',max_length=4)

# class type(models.Model):
#     """種類テーブル"""
#     typeID = models.IntegerField(verbose_name='種類ID')
#     typename = models.CharField(verbose_name='種類名',max_length=50)


class Prefecture(models.Model):
    """都道府県テーブル"""

    prefname = models.CharField(verbose_name='都道府県名',max_length=4)

    class Meta :
        verbose_name_plural = 'Prefecture'

    def __str__(self):
        return self.prefname



class Type(models.Model):
    #種類テーブル
    # typeID = models.IntegerField(verbose_name='種類ID')
    typename = models.CharField(verbose_name='種類名',max_length=50)

    class Meta : 
        verbose_name_plural = 'Type'

    def __str__(self):
        return self.typename



class Subscription(models.Model):
    #サブスクリプションテーブル
    subscription_name = models.CharField(verbose_name='サブスクリプション名',max_length=100)
    subscription_detail = models.TextField(verbose_name='サブスクリプション内容')
    subscription_rate = models.IntegerField(verbose_name='サブスクリプション料金')
    subscription_period = models.IntegerField(verbose_name='サブスクリプション期間')
    class Meta:
        verbose_name_plural = 'subscription'
    
    def __str__(self):
        return self.subscription_name



class Hospital(models.Model):
    #動物病院テーブル
    hospital_pswd = models.CharField(max_length=20,verbose_name="パスワード")    
    hospital_mail = models.EmailField(verbose_name="メールアドレス")
    hospital_name = models.CharField(max_length=30,verbose_name="病院名")
    hospital_address1 = models.ForeignKey(Prefecture,verbose_name="住所1",on_delete=models.PROTECT)
    hospital_address2 = models.CharField(max_length=100, verbose_name="住所2")
    hospital_tel = models.CharField(max_length=11,verbose_name ='固定電話番号')
    hospital_doctor = models.CharField(max_length=20,verbose_name="院長名")
    hospital_access = models.TextField(verbose_name="アクセス")
    hospital_info = models.TextField(verbose_name="お知らせ",blank=True,null= True)
    bank_name = models.CharField(max_length=4,verbose_name="銀行コード")
    bank_brunchnum = models.CharField(max_length=4,verbose_name ="支店コード")
    bank_type = models.CharField(max_length= 2,verbose_name="口座種類")
    bank_num = models.CharField(max_length= 8,verbose_name="口座番号")
    bank_hospital_name = models.CharField(max_length=30,verbose_name="口座名義")
    FK_subscriptionID = models.ForeignKey(Subscription,verbose_name="サブスクリプションID",on_delete=models.PROTECT)
    start = models.DateField(verbose_name="契約開始日",blank=True,null=True)
    end = models.DateField(verbose_name="契約終了日" ,blank=True, null=True)
    hospital_created_at= models.DateTimeField(verbose_name="作成日時",auto_now_add=True)
    hospital_updated = models.DateTimeField(verbose_name="更新日時",auto_now_add= True)

    class Meta:
        verbose_name_plural = "Hospital"

    def __str__(self):
        return self.hospital_name


class Ok(models.Model):
    #診察可能動物テーブル

    hospitalID = models.ForeignKey(Hospital, verbose_name="病院ID", on_delete= models.PROTECT)
    typeID = models.ForeignKey(Type,verbose_name="種類ID", on_delete= models.PROTECT)

    class Meta:
        verbose_name_plural = "Ok"



class CustomUser(AbstractUser):
    #利用者モデル

    
    username = models.CharField(max_length=50, verbose_name='氏名', unique=True)
    user_address1 = models.ForeignKey(Prefecture,verbose_name="住所1",on_delete=models.PROTECT)
    user_address2 = models.CharField(max_length=100, verbose_name="住所2")
    user_tel = models.IntegerField(verbose_name ='電話番号')
    email = models.EmailField(verbose_name="メールアドレス", )
    password = models.CharField(max_length=20,verbose_name="パスワード")
    user_hospital = models.ForeignKey(Hospital,verbose_name="病院ID",on_delete=models.PROTECT)
    user_created_at= models.DateTimeField(verbose_name="作成日時",auto_now_add=True)
    user_updated = models.DateTimeField(verbose_name="更新日時",auto_now= True)
    
    class Meta:
        verbose_name_plural = 'User'

'''
class Pet(models.Model):
    #ペットテーブル

    FK_pet_user = models.ForeignKey(User,verbose_name='飼い主',on_delete=models.PROTECT)
    pet_name = models.CharField(max_length=40, verbose_name='名前')
    FK_pet_typeID = models.ForeignKey(Type,verbose_name='種類',on_delete=models.PROTECT)
    pet_sex = models.CharField(max_length=5,verbose_name='性別')
    pet_birth = models.DateField(verbose_name='生年月日',null=True,blank=True)
    pet_injury = models.CharField(max_length=300,verbose_name='過去のけが',null=True,blank=True)
    pet_vaccine = models.CharField(max_length=100,verbose_name='ワクチン接種記録',null=True,blank=True)
    pet_disease = models.CharField(max_length=100,verbose_name='病気の有無',null=True,blank=True)
    pet_breeding = models.CharField(max_length=10,verbose_name='生育環境') #1:屋内　2:屋外　などを選ばせる
    pet_created = models.DateField(verbose_name='登録日',auto_now_add=True)
    pet_picture = models.ImageField(verbose_name='写真',null=True,blank=True)

    class Meta:
        verbose_name_plural = "Pet"

    def __str__(self):
        return self.pet_name
    

class Record(models.Model):
    #成長記録テーブル   

    FK_petID = models.ForeignKey(Pet,verbose_name='ペットID',on_delete=models.PROTECT)
    record_weight = models.FloatField(verbose_name='体重')
    record_food = models.IntegerField(verbose_name='ご飯')#1:完食　2:半分食べた　3:食べない　などを選ばせる
    record_update = models.DateTimeField(verbose_name="更新日時",auto_now= True)

    class Meta:
        verbose_name_plural = "Record"


class Interview(models.Model):
    #問診票テーブル

    FK_petID = models.ForeignKey(Pet,verbose_name='ペットID',on_delete=models.PROTECT)
    interview_examination = models.IntegerField(verbose_name='診察内容') #選ばせる
    interview_reason = models.TextField(verbose_name='来院理由')
    interview_picture1 = models.ImageField(verbose_name='写真1',null=True,blank=True)
    interview_picture2 = models.ImageField(verbose_name='写真2',null=True,blank=True)
    interview_picture3 = models.ImageField(verbose_name='写真3',null=True,blank=True)
    interview_create = models.DateTimeField(verbose_name="作成日時",auto_now_add=True)

    class Meta:
        verbose_name_plural = "Interview"


class Reserve(models.Model):
    #予約テーブル

    FK_userID = models.ForeignKey(User,verbose_name='利用者ID',on_delete=models.PROTECT)
    FK_hospitalID = models.ForeignKey(Hospital,verbose_name='病院ID',on_delete=models.PROTECT)
    FK_interviewID = models.ForeignKey(Interview,verbose_name='問診票ID',on_delete=models.PROTECT)
    FK_petID = models.ForeignKey(Pet,verbose_name='ペットID',on_delete=models.PROTECT)
    reserve_date = models.DateField(verbose_name="日付")
    reserve_time = models.TimeField(verbose_name="時間")
    reserve_create = models.DateTimeField(verbose_name="作成日時",auto_now_add=True)
    reserve_updated = models.DateTimeField(verbose_name="診察完了日時",null=True,blank=True)#完了ボタンを押したときに更新

    class Meta:
        verbose_name_plural = "Reserve"


class Info(models.Model):
    #お知らせテーブル

    hospitalID = models.ForeignKey(Hospital,verbose_name="病院ID", on_delete= models.PROTECT)
    title = models.CharField(max_length=50, verbose_name="タイトル")
    contents = models.TextField(verbose_name="内容")
    created = models.DateTimeField(verbose_name="作成日時", auto_now_add= True)
    updates = models.DateTimeField(verbose_name="更新日時",auto_now= True)

    class Meta:
        verbose_name_plural = "Info"

    def __str__(self):
        return self.title


class Inquiry(models.Model):
    #問合せテーブル
    
    hospitalID = models.ForeignKey(Hospital,verbose_name="病院ID", on_delete= models.PROTECT)
    UserID = models.ForeignKey(User,verbose_name="利用者ID",on_delete= models.PROTECT)
    email = models.EmailField(verbose_name="メールアドレス")
    title = models.CharField(max_length=50, verbose_name="タイトル")
    message = models.TextField(verbose_name="お問合せ内容")
    reply = models.TextField(verbose_name="返信内容",blank=True,null=True)
    created = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)

    class Meta:
        verbose_name_plural = "Inquiry"
    
    def __str__(self):
        return self.title

'''