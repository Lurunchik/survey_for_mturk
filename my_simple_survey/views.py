import re

from . import models
from ._builtin import Page

from django.template.response import TemplateResponse


class Preview(Page):
    pass


class NoFuckingCheckedTemplateResponse(TemplateResponse):
    @property
    def rendered_content(self):
        result = super().rendered_content
        return re.sub('checked', '', result)


class JokePage(Page):
    form_model = models.Player
    form_fields = ['joke_score']

    def render_to_response(self, context):
        """
        Given a context dictionary, returns an HTTP response.
        """
        return NoFuckingCheckedTemplateResponse(
            request=self.request,
            template=self.get_template_names(),
            context=context
        )

    def _increment_index_in_pages(self):
        models.JokeScore.objects.create(
            joke=self.player.joke_id,
            player=self.player.id,
            score=self.player.joke_score,
        )

        super()._increment_index_in_pages()


class Joke1(JokePage):
    template_name = 'my_simple_survey/Joke1.html'


class Joke2(JokePage):
    template_name = 'my_simple_survey/Joke2.html'


class Joke3(JokePage):
    template_name = 'my_simple_survey/Joke3.html'


class Joke4(JokePage):
    template_name = 'my_simple_survey/Joke4.html'


class Joke5(JokePage):
    template_name = 'my_simple_survey/Joke5.html'


class Joke6(JokePage):
    template_name = 'my_simple_survey/Joke6.html'


class Joke7(JokePage):
    template_name = 'my_simple_survey/Joke7.html'


class Joke8(JokePage):
    template_name = 'my_simple_survey/Joke8.html'


class Joke9(JokePage):
    template_name = 'my_simple_survey/Joke9.html'


class Joke10(JokePage):
    template_name = 'my_simple_survey/Joke10.html'


class Joke11(JokePage):
    template_name = 'my_simple_survey/Joke11.html'


class Joke12(JokePage):
    template_name = 'my_simple_survey/Joke12.html'


class Joke13(JokePage):
    template_name = 'my_simple_survey/Joke13.html'


class Joke14(JokePage):
    template_name = 'my_simple_survey/Joke14.html'


class Joke15(JokePage):
    template_name = 'my_simple_survey/Joke15.html'


class Joke16(JokePage):
    template_name = 'my_simple_survey/Joke16.html'


class Joke17(JokePage):
    template_name = 'my_simple_survey/Joke17.html'


class Joke18(JokePage):
    template_name = 'my_simple_survey/Joke18.html'


class Joke19(JokePage):
    template_name = 'my_simple_survey/Joke19.html'


class Joke20(JokePage):
    template_name = 'my_simple_survey/Joke20.html'


class Joke21(JokePage):
    template_name = 'my_simple_survey/Joke21.html'


class Joke22(JokePage):
    template_name = 'my_simple_survey/Joke22.html'


class Joke23(JokePage):
    template_name = 'my_simple_survey/Joke23.html'


class Joke24(JokePage):
    template_name = 'my_simple_survey/Joke24.html'


class Joke25(JokePage):
    template_name = 'my_simple_survey/Joke25.html'


class Joke26(JokePage):
    template_name = 'my_simple_survey/Joke26.html'


class Joke27(JokePage):
    template_name = 'my_simple_survey/Joke27.html'


class Joke28(JokePage):
    template_name = 'my_simple_survey/Joke28.html'


class Joke29(JokePage):
    template_name = 'my_simple_survey/Joke29.html'


class Joke30(JokePage):
    template_name = 'my_simple_survey/Joke30.html'


class Joke31(JokePage):
    template_name = 'my_simple_survey/Joke31.html'


class Joke32(JokePage):
    template_name = 'my_simple_survey/Joke32.html'


class Joke33(JokePage):
    template_name = 'my_simple_survey/Joke33.html'


class Joke34(JokePage):
    template_name = 'my_simple_survey/Joke34.html'


class Joke35(JokePage):
    template_name = 'my_simple_survey/Joke35.html'


class Joke36(JokePage):
    template_name = 'my_simple_survey/Joke36.html'


class Joke37(JokePage):
    template_name = 'my_simple_survey/Joke37.html'


class Joke38(JokePage):
    template_name = 'my_simple_survey/Joke38.html'


class Joke39(JokePage):
    template_name = 'my_simple_survey/Joke39.html'


class Joke40(JokePage):
    template_name = 'my_simple_survey/Joke40.html'


class Joke41(JokePage):
    template_name = 'my_simple_survey/Joke41.html'


class Joke42(JokePage):
    template_name = 'my_simple_survey/Joke42.html'


class Joke43(JokePage):
    template_name = 'my_simple_survey/Joke43.html'


class Joke44(JokePage):
    template_name = 'my_simple_survey/Joke44.html'


class Joke45(JokePage):
    template_name = 'my_simple_survey/Joke45.html'


class Joke46(JokePage):
    template_name = 'my_simple_survey/Joke46.html'


class Joke47(JokePage):
    template_name = 'my_simple_survey/Joke47.html'


class Joke48(JokePage):
    template_name = 'my_simple_survey/Joke48.html'


class Joke49(JokePage):
    template_name = 'my_simple_survey/Joke49.html'


class Joke50(JokePage):
    template_name = 'my_simple_survey/Joke50.html'


class Joke51(JokePage):
    template_name = 'my_simple_survey/Joke51.html'


class Joke52(JokePage):
    template_name = 'my_simple_survey/Joke52.html'


class Joke53(JokePage):
    template_name = 'my_simple_survey/Joke53.html'


class Joke54(JokePage):
    template_name = 'my_simple_survey/Joke54.html'


class Joke55(JokePage):
    template_name = 'my_simple_survey/Joke55.html'


class Joke56(JokePage):
    template_name = 'my_simple_survey/Joke56.html'


class Joke57(JokePage):
    template_name = 'my_simple_survey/Joke57.html'


class Joke58(JokePage):
    template_name = 'my_simple_survey/Joke58.html'


class Joke59(JokePage):
    template_name = 'my_simple_survey/Joke59.html'


class Joke60(JokePage):
    template_name = 'my_simple_survey/Joke60.html'


class Joke61(JokePage):
    template_name = 'my_simple_survey/Joke61.html'


class Joke62(JokePage):
    template_name = 'my_simple_survey/Joke62.html'


class Joke63(JokePage):
    template_name = 'my_simple_survey/Joke63.html'


class Joke64(JokePage):
    template_name = 'my_simple_survey/Joke64.html'


class Joke65(JokePage):
    template_name = 'my_simple_survey/Joke65.html'


class Joke66(JokePage):
    template_name = 'my_simple_survey/Joke66.html'


class Joke67(JokePage):
    template_name = 'my_simple_survey/Joke67.html'


class Joke68(JokePage):
    template_name = 'my_simple_survey/Joke68.html'


class Joke69(JokePage):
    template_name = 'my_simple_survey/Joke69.html'


class Joke70(JokePage):
    template_name = 'my_simple_survey/Joke70.html'


class Joke71(JokePage):
    template_name = 'my_simple_survey/Joke71.html'


class Joke72(JokePage):
    template_name = 'my_simple_survey/Joke72.html'


class Joke73(JokePage):
    template_name = 'my_simple_survey/Joke73.html'


class Joke74(JokePage):
    template_name = 'my_simple_survey/Joke74.html'


class Joke75(JokePage):
    template_name = 'my_simple_survey/Joke75.html'


class Joke76(JokePage):
    template_name = 'my_simple_survey/Joke76.html'


class Joke77(JokePage):
    template_name = 'my_simple_survey/Joke77.html'


class Joke78(JokePage):
    template_name = 'my_simple_survey/Joke78.html'


class Joke79(JokePage):
    template_name = 'my_simple_survey/Joke79.html'


class Joke80(JokePage):
    template_name = 'my_simple_survey/Joke80.html'


class Joke81(JokePage):
    template_name = 'my_simple_survey/Joke81.html'


class Joke82(JokePage):
    template_name = 'my_simple_survey/Joke82.html'


class Joke83(JokePage):
    template_name = 'my_simple_survey/Joke83.html'


class Joke84(JokePage):
    template_name = 'my_simple_survey/Joke84.html'


class Joke85(JokePage):
    template_name = 'my_simple_survey/Joke85.html'


class Joke86(JokePage):
    template_name = 'my_simple_survey/Joke86.html'


class Joke87(JokePage):
    template_name = 'my_simple_survey/Joke87.html'


class Joke88(JokePage):
    template_name = 'my_simple_survey/Joke88.html'


class Joke89(JokePage):
    template_name = 'my_simple_survey/Joke89.html'


class Joke90(JokePage):
    template_name = 'my_simple_survey/Joke90.html'


class Joke91(JokePage):
    template_name = 'my_simple_survey/Joke91.html'


class Joke92(JokePage):
    template_name = 'my_simple_survey/Joke92.html'


class Joke93(JokePage):
    template_name = 'my_simple_survey/Joke93.html'


class Joke94(JokePage):
    template_name = 'my_simple_survey/Joke94.html'


class Joke95(JokePage):
    template_name = 'my_simple_survey/Joke95.html'


class Joke96(JokePage):
    template_name = 'my_simple_survey/Joke96.html'


class Joke97(JokePage):
    template_name = 'my_simple_survey/Joke97.html'


class Joke98(JokePage):
    template_name = 'my_simple_survey/Joke98.html'


class Joke99(JokePage):
    template_name = 'my_simple_survey/Joke99.html'


class Joke100(JokePage):
    template_name = 'my_simple_survey/Joke100.html'


class Joke101(JokePage):
    template_name = 'my_simple_survey/Joke101.html'


class Joke102(JokePage):
    template_name = 'my_simple_survey/Joke102.html'


class Joke103(JokePage):
    template_name = 'my_simple_survey/Joke103.html'


class Joke104(JokePage):
    template_name = 'my_simple_survey/Joke104.html'


class Joke105(JokePage):
    template_name = 'my_simple_survey/Joke105.html'


class Joke106(JokePage):
    template_name = 'my_simple_survey/Joke106.html'


class Joke107(JokePage):
    template_name = 'my_simple_survey/Joke107.html'


class Joke108(JokePage):
    template_name = 'my_simple_survey/Joke108.html'


class Joke109(JokePage):
    template_name = 'my_simple_survey/Joke109.html'


class Joke110(JokePage):
    template_name = 'my_simple_survey/Joke110.html'


class Joke111(JokePage):
    template_name = 'my_simple_survey/Joke111.html'


class Joke112(JokePage):
    template_name = 'my_simple_survey/Joke112.html'


class Joke113(JokePage):
    template_name = 'my_simple_survey/Joke113.html'


class Joke114(JokePage):
    template_name = 'my_simple_survey/Joke114.html'


class Joke115(JokePage):
    template_name = 'my_simple_survey/Joke115.html'


class Joke116(JokePage):
    template_name = 'my_simple_survey/Joke116.html'


class Joke117(JokePage):
    template_name = 'my_simple_survey/Joke117.html'


class Joke118(JokePage):
    template_name = 'my_simple_survey/Joke118.html'


class Joke119(JokePage):
    template_name = 'my_simple_survey/Joke119.html'


class Joke120(JokePage):
    template_name = 'my_simple_survey/Joke120.html'


class Joke121(JokePage):
    template_name = 'my_simple_survey/Joke121.html'


class Joke122(JokePage):
    template_name = 'my_simple_survey/Joke122.html'


class Joke123(JokePage):
    template_name = 'my_simple_survey/Joke123.html'


class Joke124(JokePage):
    template_name = 'my_simple_survey/Joke124.html'


class Joke125(JokePage):
    template_name = 'my_simple_survey/Joke125.html'


class Joke126(JokePage):
    template_name = 'my_simple_survey/Joke126.html'


class Joke127(JokePage):
    template_name = 'my_simple_survey/Joke127.html'


class Joke128(JokePage):
    template_name = 'my_simple_survey/Joke128.html'


class Joke129(JokePage):
    template_name = 'my_simple_survey/Joke129.html'


class Joke130(JokePage):
    template_name = 'my_simple_survey/Joke130.html'


class Joke131(JokePage):
    template_name = 'my_simple_survey/Joke131.html'


class Joke132(JokePage):
    template_name = 'my_simple_survey/Joke132.html'


class Joke133(JokePage):
    template_name = 'my_simple_survey/Joke133.html'


class Joke134(JokePage):
    template_name = 'my_simple_survey/Joke134.html'


class Joke135(JokePage):
    template_name = 'my_simple_survey/Joke135.html'


class Joke136(JokePage):
    template_name = 'my_simple_survey/Joke136.html'


class Joke137(JokePage):
    template_name = 'my_simple_survey/Joke137.html'


class Joke138(JokePage):
    template_name = 'my_simple_survey/Joke138.html'


class Joke139(JokePage):
    template_name = 'my_simple_survey/Joke139.html'


class Joke140(JokePage):
    template_name = 'my_simple_survey/Joke140.html'


class Joke141(JokePage):
    template_name = 'my_simple_survey/Joke141.html'


class Joke142(JokePage):
    template_name = 'my_simple_survey/Joke142.html'


class Joke143(JokePage):
    template_name = 'my_simple_survey/Joke143.html'


class Joke144(JokePage):
    template_name = 'my_simple_survey/Joke144.html'


class Joke145(JokePage):
    template_name = 'my_simple_survey/Joke145.html'


class Joke146(JokePage):
    template_name = 'my_simple_survey/Joke146.html'


class Joke147(JokePage):
    template_name = 'my_simple_survey/Joke147.html'


class Joke148(JokePage):
    template_name = 'my_simple_survey/Joke148.html'


class Joke149(JokePage):
    template_name = 'my_simple_survey/Joke149.html'


class Joke150(JokePage):
    template_name = 'my_simple_survey/Joke150.html'


class Joke151(JokePage):
    template_name = 'my_simple_survey/Joke151.html'


class Joke152(JokePage):
    template_name = 'my_simple_survey/Joke152.html'


class Joke153(JokePage):
    template_name = 'my_simple_survey/Joke153.html'


class Joke154(JokePage):
    template_name = 'my_simple_survey/Joke154.html'


class Joke155(JokePage):
    template_name = 'my_simple_survey/Joke155.html'


class Joke156(JokePage):
    template_name = 'my_simple_survey/Joke156.html'


class Joke157(JokePage):
    template_name = 'my_simple_survey/Joke157.html'


class Joke158(JokePage):
    template_name = 'my_simple_survey/Joke158.html'


class Joke159(JokePage):
    template_name = 'my_simple_survey/Joke159.html'


class Joke160(JokePage):
    template_name = 'my_simple_survey/Joke160.html'


class Joke161(JokePage):
    template_name = 'my_simple_survey/Joke161.html'


class Joke162(JokePage):
    template_name = 'my_simple_survey/Joke162.html'


class Joke163(JokePage):
    template_name = 'my_simple_survey/Joke163.html'


class Joke164(JokePage):
    template_name = 'my_simple_survey/Joke164.html'


class Joke165(JokePage):
    template_name = 'my_simple_survey/Joke165.html'


class Joke166(JokePage):
    template_name = 'my_simple_survey/Joke166.html'


class Joke167(JokePage):
    template_name = 'my_simple_survey/Joke167.html'


class Joke168(JokePage):
    template_name = 'my_simple_survey/Joke168.html'


class Joke169(JokePage):
    template_name = 'my_simple_survey/Joke169.html'


class Joke170(JokePage):
    template_name = 'my_simple_survey/Joke170.html'


class Joke171(JokePage):
    template_name = 'my_simple_survey/Joke171.html'


class Joke172(JokePage):
    template_name = 'my_simple_survey/Joke172.html'


class Joke173(JokePage):
    template_name = 'my_simple_survey/Joke173.html'


class Joke174(JokePage):
    template_name = 'my_simple_survey/Joke174.html'


class Joke175(JokePage):
    template_name = 'my_simple_survey/Joke175.html'


class Joke176(JokePage):
    template_name = 'my_simple_survey/Joke176.html'


class Joke177(JokePage):
    template_name = 'my_simple_survey/Joke177.html'


class Joke178(JokePage):
    template_name = 'my_simple_survey/Joke178.html'


class Joke179(JokePage):
    template_name = 'my_simple_survey/Joke179.html'


class Joke180(JokePage):
    template_name = 'my_simple_survey/Joke180.html'


class Joke181(JokePage):
    template_name = 'my_simple_survey/Joke181.html'


class Joke182(JokePage):
    template_name = 'my_simple_survey/Joke182.html'


class Joke183(JokePage):
    template_name = 'my_simple_survey/Joke183.html'


class Joke184(JokePage):
    template_name = 'my_simple_survey/Joke184.html'


class Joke185(JokePage):
    template_name = 'my_simple_survey/Joke185.html'


class Joke186(JokePage):
    template_name = 'my_simple_survey/Joke186.html'


class Joke187(JokePage):
    template_name = 'my_simple_survey/Joke187.html'


class Joke188(JokePage):
    template_name = 'my_simple_survey/Joke188.html'


class Joke189(JokePage):
    template_name = 'my_simple_survey/Joke189.html'


class Joke190(JokePage):
    template_name = 'my_simple_survey/Joke190.html'


class Joke191(JokePage):
    template_name = 'my_simple_survey/Joke191.html'


class Joke192(JokePage):
    template_name = 'my_simple_survey/Joke192.html'


class Joke193(JokePage):
    template_name = 'my_simple_survey/Joke193.html'


class Joke194(JokePage):
    template_name = 'my_simple_survey/Joke194.html'


class Joke195(JokePage):
    template_name = 'my_simple_survey/Joke195.html'


class Joke196(JokePage):
    template_name = 'my_simple_survey/Joke196.html'


class Joke197(JokePage):
    template_name = 'my_simple_survey/Joke197.html'


class Joke198(JokePage):
    template_name = 'my_simple_survey/Joke198.html'


class Joke199(JokePage):
    template_name = 'my_simple_survey/Joke199.html'


class Joke200(JokePage):
    template_name = 'my_simple_survey/Joke200.html'


class Joke201(JokePage):
    template_name = 'my_simple_survey/Joke201.html'


class Joke202(JokePage):
    template_name = 'my_simple_survey/Joke202.html'


class Joke203(JokePage):
    template_name = 'my_simple_survey/Joke203.html'


class Joke204(JokePage):
    template_name = 'my_simple_survey/Joke204.html'


class Joke205(JokePage):
    template_name = 'my_simple_survey/Joke205.html'


class Joke206(JokePage):
    template_name = 'my_simple_survey/Joke206.html'


class Joke207(JokePage):
    template_name = 'my_simple_survey/Joke207.html'


class Joke208(JokePage):
    template_name = 'my_simple_survey/Joke208.html'


class Joke209(JokePage):
    template_name = 'my_simple_survey/Joke209.html'


class Joke210(JokePage):
    template_name = 'my_simple_survey/Joke210.html'


class Joke211(JokePage):
    template_name = 'my_simple_survey/Joke211.html'


class Joke212(JokePage):
    template_name = 'my_simple_survey/Joke212.html'


class Joke213(JokePage):
    template_name = 'my_simple_survey/Joke213.html'


class Joke214(JokePage):
    template_name = 'my_simple_survey/Joke214.html'


class Joke215(JokePage):
    template_name = 'my_simple_survey/Joke215.html'


class Joke216(JokePage):
    template_name = 'my_simple_survey/Joke216.html'


class Joke217(JokePage):
    template_name = 'my_simple_survey/Joke217.html'


class Joke218(JokePage):
    template_name = 'my_simple_survey/Joke218.html'


class Joke219(JokePage):
    template_name = 'my_simple_survey/Joke219.html'


class Joke220(JokePage):
    template_name = 'my_simple_survey/Joke220.html'


class Joke221(JokePage):
    template_name = 'my_simple_survey/Joke221.html'


class Joke222(JokePage):
    template_name = 'my_simple_survey/Joke222.html'


class Joke223(JokePage):
    template_name = 'my_simple_survey/Joke223.html'


class Joke224(JokePage):
    template_name = 'my_simple_survey/Joke224.html'


class Joke225(JokePage):
    template_name = 'my_simple_survey/Joke225.html'


class Joke226(JokePage):
    template_name = 'my_simple_survey/Joke226.html'


class Joke227(JokePage):
    template_name = 'my_simple_survey/Joke227.html'


class Joke228(JokePage):
    template_name = 'my_simple_survey/Joke228.html'


class Joke229(JokePage):
    template_name = 'my_simple_survey/Joke229.html'


class Joke230(JokePage):
    template_name = 'my_simple_survey/Joke230.html'


class Joke231(JokePage):
    template_name = 'my_simple_survey/Joke231.html'


class Joke232(JokePage):
    template_name = 'my_simple_survey/Joke232.html'


class Joke233(JokePage):
    template_name = 'my_simple_survey/Joke233.html'


class Joke234(JokePage):
    template_name = 'my_simple_survey/Joke234.html'


class Joke235(JokePage):
    template_name = 'my_simple_survey/Joke235.html'


class Joke236(JokePage):
    template_name = 'my_simple_survey/Joke236.html'


class Joke237(JokePage):
    template_name = 'my_simple_survey/Joke237.html'


class Joke238(JokePage):
    template_name = 'my_simple_survey/Joke238.html'


class Joke239(JokePage):
    template_name = 'my_simple_survey/Joke239.html'


class Joke240(JokePage):
    template_name = 'my_simple_survey/Joke240.html'


class Joke241(JokePage):
    template_name = 'my_simple_survey/Joke241.html'


class Joke242(JokePage):
    template_name = 'my_simple_survey/Joke242.html'


class Joke243(JokePage):
    template_name = 'my_simple_survey/Joke243.html'


class Joke244(JokePage):
    template_name = 'my_simple_survey/Joke244.html'


class Joke245(JokePage):
    template_name = 'my_simple_survey/Joke245.html'


class Joke246(JokePage):
    template_name = 'my_simple_survey/Joke246.html'


class Joke247(JokePage):
    template_name = 'my_simple_survey/Joke247.html'


class Joke248(JokePage):
    template_name = 'my_simple_survey/Joke248.html'


class Joke249(JokePage):
    template_name = 'my_simple_survey/Joke249.html'


class Joke250(JokePage):
    template_name = 'my_simple_survey/Joke250.html'


class Joke251(JokePage):
    template_name = 'my_simple_survey/Joke251.html'


class Joke252(JokePage):
    template_name = 'my_simple_survey/Joke252.html'


class Joke253(JokePage):
    template_name = 'my_simple_survey/Joke253.html'


class Joke254(JokePage):
    template_name = 'my_simple_survey/Joke254.html'


class Joke255(JokePage):
    template_name = 'my_simple_survey/Joke255.html'


class Joke256(JokePage):
    template_name = 'my_simple_survey/Joke256.html'


class Joke257(JokePage):
    template_name = 'my_simple_survey/Joke257.html'


class Joke258(JokePage):
    template_name = 'my_simple_survey/Joke258.html'


class Joke259(JokePage):
    template_name = 'my_simple_survey/Joke259.html'


class Joke260(JokePage):
    template_name = 'my_simple_survey/Joke260.html'


class Joke261(JokePage):
    template_name = 'my_simple_survey/Joke261.html'


class Joke262(JokePage):
    template_name = 'my_simple_survey/Joke262.html'


class Joke263(JokePage):
    template_name = 'my_simple_survey/Joke263.html'


class Joke264(JokePage):
    template_name = 'my_simple_survey/Joke264.html'


class Joke265(JokePage):
    template_name = 'my_simple_survey/Joke265.html'


class Joke266(JokePage):
    template_name = 'my_simple_survey/Joke266.html'


class Joke267(JokePage):
    template_name = 'my_simple_survey/Joke267.html'


class Joke268(JokePage):
    template_name = 'my_simple_survey/Joke268.html'


class Joke269(JokePage):
    template_name = 'my_simple_survey/Joke269.html'


class Joke270(JokePage):
    template_name = 'my_simple_survey/Joke270.html'


class Joke271(JokePage):
    template_name = 'my_simple_survey/Joke271.html'


class Joke272(JokePage):
    template_name = 'my_simple_survey/Joke272.html'


class Joke273(JokePage):
    template_name = 'my_simple_survey/Joke273.html'


class Joke274(JokePage):
    template_name = 'my_simple_survey/Joke274.html'


class Joke275(JokePage):
    template_name = 'my_simple_survey/Joke275.html'


class Joke276(JokePage):
    template_name = 'my_simple_survey/Joke276.html'


class Joke277(JokePage):
    template_name = 'my_simple_survey/Joke277.html'


class Joke278(JokePage):
    template_name = 'my_simple_survey/Joke278.html'


class Joke279(JokePage):
    template_name = 'my_simple_survey/Joke279.html'


class Joke280(JokePage):
    template_name = 'my_simple_survey/Joke280.html'


class Joke281(JokePage):
    template_name = 'my_simple_survey/Joke281.html'


class Joke282(JokePage):
    template_name = 'my_simple_survey/Joke282.html'


class Joke283(JokePage):
    template_name = 'my_simple_survey/Joke283.html'


class Joke284(JokePage):
    template_name = 'my_simple_survey/Joke284.html'


class Joke285(JokePage):
    template_name = 'my_simple_survey/Joke285.html'


class Joke286(JokePage):
    template_name = 'my_simple_survey/Joke286.html'


class Joke287(JokePage):
    template_name = 'my_simple_survey/Joke287.html'


class Joke288(JokePage):
    template_name = 'my_simple_survey/Joke288.html'


class Joke289(JokePage):
    template_name = 'my_simple_survey/Joke289.html'


class Joke290(JokePage):
    template_name = 'my_simple_survey/Joke290.html'


class Joke291(JokePage):
    template_name = 'my_simple_survey/Joke291.html'


class Joke292(JokePage):
    template_name = 'my_simple_survey/Joke292.html'


class Joke293(JokePage):
    template_name = 'my_simple_survey/Joke293.html'


class Joke294(JokePage):
    template_name = 'my_simple_survey/Joke294.html'


class Joke295(JokePage):
    template_name = 'my_simple_survey/Joke295.html'


class Joke296(JokePage):
    template_name = 'my_simple_survey/Joke296.html'


class Joke297(JokePage):
    template_name = 'my_simple_survey/Joke297.html'


class Joke298(JokePage):
    template_name = 'my_simple_survey/Joke298.html'


class Joke299(JokePage):
    template_name = 'my_simple_survey/Joke299.html'


class Joke300(JokePage):
    template_name = 'my_simple_survey/Joke300.html'


class Joke301(JokePage):
    template_name = 'my_simple_survey/Joke301.html'


class Joke302(JokePage):
    template_name = 'my_simple_survey/Joke302.html'


class Joke303(JokePage):
    template_name = 'my_simple_survey/Joke303.html'


class Joke304(JokePage):
    template_name = 'my_simple_survey/Joke304.html'


class Joke305(JokePage):
    template_name = 'my_simple_survey/Joke305.html'


class Joke306(JokePage):
    template_name = 'my_simple_survey/Joke306.html'


class Joke307(JokePage):
    template_name = 'my_simple_survey/Joke307.html'


class Joke308(JokePage):
    template_name = 'my_simple_survey/Joke308.html'


class Joke309(JokePage):
    template_name = 'my_simple_survey/Joke309.html'


class Joke310(JokePage):
    template_name = 'my_simple_survey/Joke310.html'


class Joke311(JokePage):
    template_name = 'my_simple_survey/Joke311.html'


class Joke312(JokePage):
    template_name = 'my_simple_survey/Joke312.html'


class Joke313(JokePage):
    template_name = 'my_simple_survey/Joke313.html'


class Joke314(JokePage):
    template_name = 'my_simple_survey/Joke314.html'


class Joke315(JokePage):
    template_name = 'my_simple_survey/Joke315.html'


class Joke316(JokePage):
    template_name = 'my_simple_survey/Joke316.html'


class Joke317(JokePage):
    template_name = 'my_simple_survey/Joke317.html'


class Joke318(JokePage):
    template_name = 'my_simple_survey/Joke318.html'


class Joke319(JokePage):
    template_name = 'my_simple_survey/Joke319.html'


class Joke320(JokePage):
    template_name = 'my_simple_survey/Joke320.html'


class Joke321(JokePage):
    template_name = 'my_simple_survey/Joke321.html'


class Joke322(JokePage):
    template_name = 'my_simple_survey/Joke322.html'


class Joke323(JokePage):
    template_name = 'my_simple_survey/Joke323.html'


class Joke324(JokePage):
    template_name = 'my_simple_survey/Joke324.html'


class Joke325(JokePage):
    template_name = 'my_simple_survey/Joke325.html'


class Joke326(JokePage):
    template_name = 'my_simple_survey/Joke326.html'


class Joke327(JokePage):
    template_name = 'my_simple_survey/Joke327.html'


class Joke328(JokePage):
    template_name = 'my_simple_survey/Joke328.html'


class Joke329(JokePage):
    template_name = 'my_simple_survey/Joke329.html'


class Joke330(JokePage):
    template_name = 'my_simple_survey/Joke330.html'


class Joke331(JokePage):
    template_name = 'my_simple_survey/Joke331.html'


class Joke332(JokePage):
    template_name = 'my_simple_survey/Joke332.html'


class Joke333(JokePage):
    template_name = 'my_simple_survey/Joke333.html'


class Joke334(JokePage):
    template_name = 'my_simple_survey/Joke334.html'


class Joke335(JokePage):
    template_name = 'my_simple_survey/Joke335.html'


class Joke336(JokePage):
    template_name = 'my_simple_survey/Joke336.html'


class Joke337(JokePage):
    template_name = 'my_simple_survey/Joke337.html'


class Joke338(JokePage):
    template_name = 'my_simple_survey/Joke338.html'


class Joke339(JokePage):
    template_name = 'my_simple_survey/Joke339.html'


class Joke340(JokePage):
    template_name = 'my_simple_survey/Joke340.html'


class Joke341(JokePage):
    template_name = 'my_simple_survey/Joke341.html'


class Joke342(JokePage):
    template_name = 'my_simple_survey/Joke342.html'


class Joke343(JokePage):
    template_name = 'my_simple_survey/Joke343.html'


class Joke344(JokePage):
    template_name = 'my_simple_survey/Joke344.html'


class Joke345(JokePage):
    template_name = 'my_simple_survey/Joke345.html'


class Joke346(JokePage):
    template_name = 'my_simple_survey/Joke346.html'


class Joke347(JokePage):
    template_name = 'my_simple_survey/Joke347.html'


class Joke348(JokePage):
    template_name = 'my_simple_survey/Joke348.html'


class Joke349(JokePage):
    template_name = 'my_simple_survey/Joke349.html'


class Joke350(JokePage):
    template_name = 'my_simple_survey/Joke350.html'


class Joke351(JokePage):
    template_name = 'my_simple_survey/Joke351.html'


class Joke352(JokePage):
    template_name = 'my_simple_survey/Joke352.html'


class Joke353(JokePage):
    template_name = 'my_simple_survey/Joke353.html'


class Joke354(JokePage):
    template_name = 'my_simple_survey/Joke354.html'


class Joke355(JokePage):
    template_name = 'my_simple_survey/Joke355.html'


class Joke356(JokePage):
    template_name = 'my_simple_survey/Joke356.html'


class Joke357(JokePage):
    template_name = 'my_simple_survey/Joke357.html'


class Joke358(JokePage):
    template_name = 'my_simple_survey/Joke358.html'


class Joke359(JokePage):
    template_name = 'my_simple_survey/Joke359.html'


class Joke360(JokePage):
    template_name = 'my_simple_survey/Joke360.html'


class Joke361(JokePage):
    template_name = 'my_simple_survey/Joke361.html'


class Joke362(JokePage):
    template_name = 'my_simple_survey/Joke362.html'


class Joke363(JokePage):
    template_name = 'my_simple_survey/Joke363.html'


class Joke364(JokePage):
    template_name = 'my_simple_survey/Joke364.html'


class Joke365(JokePage):
    template_name = 'my_simple_survey/Joke365.html'


class Joke366(JokePage):
    template_name = 'my_simple_survey/Joke366.html'


class Joke367(JokePage):
    template_name = 'my_simple_survey/Joke367.html'


class Joke368(JokePage):
    template_name = 'my_simple_survey/Joke368.html'


class Joke369(JokePage):
    template_name = 'my_simple_survey/Joke369.html'


class Joke370(JokePage):
    template_name = 'my_simple_survey/Joke370.html'


class Joke371(JokePage):
    template_name = 'my_simple_survey/Joke371.html'


class Joke372(JokePage):
    template_name = 'my_simple_survey/Joke372.html'


class Joke373(JokePage):
    template_name = 'my_simple_survey/Joke373.html'


class Joke374(JokePage):
    template_name = 'my_simple_survey/Joke374.html'


class Joke375(JokePage):
    template_name = 'my_simple_survey/Joke375.html'


class Joke376(JokePage):
    template_name = 'my_simple_survey/Joke376.html'


class Joke377(JokePage):
    template_name = 'my_simple_survey/Joke377.html'


class Joke378(JokePage):
    template_name = 'my_simple_survey/Joke378.html'


class Joke379(JokePage):
    template_name = 'my_simple_survey/Joke379.html'


class Joke380(JokePage):
    template_name = 'my_simple_survey/Joke380.html'


class Joke381(JokePage):
    template_name = 'my_simple_survey/Joke381.html'


class Joke382(JokePage):
    template_name = 'my_simple_survey/Joke382.html'


class Joke383(JokePage):
    template_name = 'my_simple_survey/Joke383.html'


class Joke384(JokePage):
    template_name = 'my_simple_survey/Joke384.html'


class Joke385(JokePage):
    template_name = 'my_simple_survey/Joke385.html'


class Joke386(JokePage):
    template_name = 'my_simple_survey/Joke386.html'


class Joke387(JokePage):
    template_name = 'my_simple_survey/Joke387.html'


class Joke388(JokePage):
    template_name = 'my_simple_survey/Joke388.html'


class Joke389(JokePage):
    template_name = 'my_simple_survey/Joke389.html'


class Joke390(JokePage):
    template_name = 'my_simple_survey/Joke390.html'


class Joke391(JokePage):
    template_name = 'my_simple_survey/Joke391.html'


class Joke392(JokePage):
    template_name = 'my_simple_survey/Joke392.html'


class Joke393(JokePage):
    template_name = 'my_simple_survey/Joke393.html'


class Joke394(JokePage):
    template_name = 'my_simple_survey/Joke394.html'


class Joke395(JokePage):
    template_name = 'my_simple_survey/Joke395.html'


class Joke396(JokePage):
    template_name = 'my_simple_survey/Joke396.html'


class Joke397(JokePage):
    template_name = 'my_simple_survey/Joke397.html'


class Joke398(JokePage):
    template_name = 'my_simple_survey/Joke398.html'


class Joke399(JokePage):
    template_name = 'my_simple_survey/Joke399.html'


class Joke400(JokePage):
    template_name = 'my_simple_survey/Joke400.html'


class Joke401(JokePage):
    template_name = 'my_simple_survey/Joke401.html'


class Joke402(JokePage):
    template_name = 'my_simple_survey/Joke402.html'


class Joke403(JokePage):
    template_name = 'my_simple_survey/Joke403.html'


class Joke404(JokePage):
    template_name = 'my_simple_survey/Joke404.html'


class Joke405(JokePage):
    template_name = 'my_simple_survey/Joke405.html'


class Joke406(JokePage):
    template_name = 'my_simple_survey/Joke406.html'


class Joke407(JokePage):
    template_name = 'my_simple_survey/Joke407.html'


class Joke408(JokePage):
    template_name = 'my_simple_survey/Joke408.html'


class Joke409(JokePage):
    template_name = 'my_simple_survey/Joke409.html'


class Joke410(JokePage):
    template_name = 'my_simple_survey/Joke410.html'


class Joke411(JokePage):
    template_name = 'my_simple_survey/Joke411.html'


class Joke412(JokePage):
    template_name = 'my_simple_survey/Joke412.html'


class Joke413(JokePage):
    template_name = 'my_simple_survey/Joke413.html'


class Joke414(JokePage):
    template_name = 'my_simple_survey/Joke414.html'


class Joke415(JokePage):
    template_name = 'my_simple_survey/Joke415.html'


class Joke416(JokePage):
    template_name = 'my_simple_survey/Joke416.html'


class Joke417(JokePage):
    template_name = 'my_simple_survey/Joke417.html'


class Joke418(JokePage):
    template_name = 'my_simple_survey/Joke418.html'


class Joke419(JokePage):
    template_name = 'my_simple_survey/Joke419.html'


class Joke420(JokePage):
    template_name = 'my_simple_survey/Joke420.html'


class Joke421(JokePage):
    template_name = 'my_simple_survey/Joke421.html'


class Joke422(JokePage):
    template_name = 'my_simple_survey/Joke422.html'


class Joke423(JokePage):
    template_name = 'my_simple_survey/Joke423.html'


class Joke424(JokePage):
    template_name = 'my_simple_survey/Joke424.html'


class Joke425(JokePage):
    template_name = 'my_simple_survey/Joke425.html'


class Joke426(JokePage):
    template_name = 'my_simple_survey/Joke426.html'


class Joke427(JokePage):
    template_name = 'my_simple_survey/Joke427.html'


class Joke428(JokePage):
    template_name = 'my_simple_survey/Joke428.html'


class Joke429(JokePage):
    template_name = 'my_simple_survey/Joke429.html'


class Joke430(JokePage):
    template_name = 'my_simple_survey/Joke430.html'


class Joke431(JokePage):
    template_name = 'my_simple_survey/Joke431.html'


class Joke432(JokePage):
    template_name = 'my_simple_survey/Joke432.html'


class Joke433(JokePage):
    template_name = 'my_simple_survey/Joke433.html'


class Joke434(JokePage):
    template_name = 'my_simple_survey/Joke434.html'


class Joke435(JokePage):
    template_name = 'my_simple_survey/Joke435.html'


class Joke436(JokePage):
    template_name = 'my_simple_survey/Joke436.html'


class Joke437(JokePage):
    template_name = 'my_simple_survey/Joke437.html'


class Joke438(JokePage):
    template_name = 'my_simple_survey/Joke438.html'


class Joke439(JokePage):
    template_name = 'my_simple_survey/Joke439.html'


class Joke440(JokePage):
    template_name = 'my_simple_survey/Joke440.html'


class Joke441(JokePage):
    template_name = 'my_simple_survey/Joke441.html'


class Joke442(JokePage):
    template_name = 'my_simple_survey/Joke442.html'


class Joke443(JokePage):
    template_name = 'my_simple_survey/Joke443.html'


class Joke444(JokePage):
    template_name = 'my_simple_survey/Joke444.html'


class Joke445(JokePage):
    template_name = 'my_simple_survey/Joke445.html'


class Joke446(JokePage):
    template_name = 'my_simple_survey/Joke446.html'


class Joke447(JokePage):
    template_name = 'my_simple_survey/Joke447.html'


class Joke448(JokePage):
    template_name = 'my_simple_survey/Joke448.html'


class Joke449(JokePage):
    template_name = 'my_simple_survey/Joke449.html'


class Joke450(JokePage):
    template_name = 'my_simple_survey/Joke450.html'


class Joke451(JokePage):
    template_name = 'my_simple_survey/Joke451.html'


class Joke452(JokePage):
    template_name = 'my_simple_survey/Joke452.html'


class Joke453(JokePage):
    template_name = 'my_simple_survey/Joke453.html'


class Joke454(JokePage):
    template_name = 'my_simple_survey/Joke454.html'


class Joke455(JokePage):
    template_name = 'my_simple_survey/Joke455.html'


class Joke456(JokePage):
    template_name = 'my_simple_survey/Joke456.html'


class Joke457(JokePage):
    template_name = 'my_simple_survey/Joke457.html'


class Joke458(JokePage):
    template_name = 'my_simple_survey/Joke458.html'


class Joke459(JokePage):
    template_name = 'my_simple_survey/Joke459.html'


class Joke460(JokePage):
    template_name = 'my_simple_survey/Joke460.html'


class Joke461(JokePage):
    template_name = 'my_simple_survey/Joke461.html'


class Joke462(JokePage):
    template_name = 'my_simple_survey/Joke462.html'


class Joke463(JokePage):
    template_name = 'my_simple_survey/Joke463.html'


class Joke464(JokePage):
    template_name = 'my_simple_survey/Joke464.html'


class Joke465(JokePage):
    template_name = 'my_simple_survey/Joke465.html'


class Joke466(JokePage):
    template_name = 'my_simple_survey/Joke466.html'


class Joke467(JokePage):
    template_name = 'my_simple_survey/Joke467.html'


class Joke468(JokePage):
    template_name = 'my_simple_survey/Joke468.html'


class Joke469(JokePage):
    template_name = 'my_simple_survey/Joke469.html'


class Joke470(JokePage):
    template_name = 'my_simple_survey/Joke470.html'


class Joke471(JokePage):
    template_name = 'my_simple_survey/Joke471.html'


class Joke472(JokePage):
    template_name = 'my_simple_survey/Joke472.html'


class Joke473(JokePage):
    template_name = 'my_simple_survey/Joke473.html'


class Joke474(JokePage):
    template_name = 'my_simple_survey/Joke474.html'


class Joke475(JokePage):
    template_name = 'my_simple_survey/Joke475.html'


class Joke476(JokePage):
    template_name = 'my_simple_survey/Joke476.html'


class Joke477(JokePage):
    template_name = 'my_simple_survey/Joke477.html'


class Joke478(JokePage):
    template_name = 'my_simple_survey/Joke478.html'


class Joke479(JokePage):
    template_name = 'my_simple_survey/Joke479.html'


class Joke480(JokePage):
    template_name = 'my_simple_survey/Joke480.html'


class Joke481(JokePage):
    template_name = 'my_simple_survey/Joke481.html'


class Joke482(JokePage):
    template_name = 'my_simple_survey/Joke482.html'


class Joke483(JokePage):
    template_name = 'my_simple_survey/Joke483.html'


class Joke484(JokePage):
    template_name = 'my_simple_survey/Joke484.html'


class Joke485(JokePage):
    template_name = 'my_simple_survey/Joke485.html'


class Joke486(JokePage):
    template_name = 'my_simple_survey/Joke486.html'


class Joke487(JokePage):
    template_name = 'my_simple_survey/Joke487.html'


class Joke488(JokePage):
    template_name = 'my_simple_survey/Joke488.html'


class Joke489(JokePage):
    template_name = 'my_simple_survey/Joke489.html'


class Joke490(JokePage):
    template_name = 'my_simple_survey/Joke490.html'


class Joke491(JokePage):
    template_name = 'my_simple_survey/Joke491.html'


class Joke492(JokePage):
    template_name = 'my_simple_survey/Joke492.html'


class Joke493(JokePage):
    template_name = 'my_simple_survey/Joke493.html'


class Joke494(JokePage):
    template_name = 'my_simple_survey/Joke494.html'


class Joke495(JokePage):
    template_name = 'my_simple_survey/Joke495.html'


class Joke496(JokePage):
    template_name = 'my_simple_survey/Joke496.html'


class Joke497(JokePage):
    template_name = 'my_simple_survey/Joke497.html'


class Joke498(JokePage):
    template_name = 'my_simple_survey/Joke498.html'


class Joke499(JokePage):
    template_name = 'my_simple_survey/Joke499.html'


class Joke500(JokePage):
    template_name = 'my_simple_survey/Joke500.html'


class Joke501(JokePage):
    template_name = 'my_simple_survey/Joke501.html'


class Joke502(JokePage):
    template_name = 'my_simple_survey/Joke502.html'


class Joke503(JokePage):
    template_name = 'my_simple_survey/Joke503.html'


class Joke504(JokePage):
    template_name = 'my_simple_survey/Joke504.html'


class Joke505(JokePage):
    template_name = 'my_simple_survey/Joke505.html'


class Joke506(JokePage):
    template_name = 'my_simple_survey/Joke506.html'


class Joke507(JokePage):
    template_name = 'my_simple_survey/Joke507.html'


class Joke508(JokePage):
    template_name = 'my_simple_survey/Joke508.html'


class Joke509(JokePage):
    template_name = 'my_simple_survey/Joke509.html'


class Joke510(JokePage):
    template_name = 'my_simple_survey/Joke510.html'


class Joke511(JokePage):
    template_name = 'my_simple_survey/Joke511.html'


class Joke512(JokePage):
    template_name = 'my_simple_survey/Joke512.html'


class Joke513(JokePage):
    template_name = 'my_simple_survey/Joke513.html'


class Joke514(JokePage):
    template_name = 'my_simple_survey/Joke514.html'


class Joke515(JokePage):
    template_name = 'my_simple_survey/Joke515.html'


class Joke516(JokePage):
    template_name = 'my_simple_survey/Joke516.html'


class Joke517(JokePage):
    template_name = 'my_simple_survey/Joke517.html'


class Joke518(JokePage):
    template_name = 'my_simple_survey/Joke518.html'


class Joke519(JokePage):
    template_name = 'my_simple_survey/Joke519.html'


class Joke520(JokePage):
    template_name = 'my_simple_survey/Joke520.html'


class Joke521(JokePage):
    template_name = 'my_simple_survey/Joke521.html'


class Joke522(JokePage):
    template_name = 'my_simple_survey/Joke522.html'


class Joke523(JokePage):
    template_name = 'my_simple_survey/Joke523.html'


class Joke524(JokePage):
    template_name = 'my_simple_survey/Joke524.html'


class Joke525(JokePage):
    template_name = 'my_simple_survey/Joke525.html'


class Joke526(JokePage):
    template_name = 'my_simple_survey/Joke526.html'


class Joke527(JokePage):
    template_name = 'my_simple_survey/Joke527.html'


class Joke528(JokePage):
    template_name = 'my_simple_survey/Joke528.html'


class Joke529(JokePage):
    template_name = 'my_simple_survey/Joke529.html'


class Joke530(JokePage):
    template_name = 'my_simple_survey/Joke530.html'


class Joke531(JokePage):
    template_name = 'my_simple_survey/Joke531.html'


class Joke532(JokePage):
    template_name = 'my_simple_survey/Joke532.html'


class Joke533(JokePage):
    template_name = 'my_simple_survey/Joke533.html'


class Joke534(JokePage):
    template_name = 'my_simple_survey/Joke534.html'


class Joke535(JokePage):
    template_name = 'my_simple_survey/Joke535.html'


class Joke536(JokePage):
    template_name = 'my_simple_survey/Joke536.html'


class Joke537(JokePage):
    template_name = 'my_simple_survey/Joke537.html'


class Joke538(JokePage):
    template_name = 'my_simple_survey/Joke538.html'


class Joke539(JokePage):
    template_name = 'my_simple_survey/Joke539.html'


class Joke540(JokePage):
    template_name = 'my_simple_survey/Joke540.html'


class Joke541(JokePage):
    template_name = 'my_simple_survey/Joke541.html'


class Joke542(JokePage):
    template_name = 'my_simple_survey/Joke542.html'


class Joke543(JokePage):
    template_name = 'my_simple_survey/Joke543.html'


class Joke544(JokePage):
    template_name = 'my_simple_survey/Joke544.html'


class Joke545(JokePage):
    template_name = 'my_simple_survey/Joke545.html'


class Joke546(JokePage):
    template_name = 'my_simple_survey/Joke546.html'


class Joke547(JokePage):
    template_name = 'my_simple_survey/Joke547.html'


class Joke548(JokePage):
    template_name = 'my_simple_survey/Joke548.html'


class Joke549(JokePage):
    template_name = 'my_simple_survey/Joke549.html'


class Joke550(JokePage):
    template_name = 'my_simple_survey/Joke550.html'


class Joke551(JokePage):
    template_name = 'my_simple_survey/Joke551.html'


class Joke552(JokePage):
    template_name = 'my_simple_survey/Joke552.html'


class Joke553(JokePage):
    template_name = 'my_simple_survey/Joke553.html'


class Joke554(JokePage):
    template_name = 'my_simple_survey/Joke554.html'


class Joke555(JokePage):
    template_name = 'my_simple_survey/Joke555.html'


class Joke556(JokePage):
    template_name = 'my_simple_survey/Joke556.html'


class Joke557(JokePage):
    template_name = 'my_simple_survey/Joke557.html'


class Joke558(JokePage):
    template_name = 'my_simple_survey/Joke558.html'


class Joke559(JokePage):
    template_name = 'my_simple_survey/Joke559.html'


class Joke560(JokePage):
    template_name = 'my_simple_survey/Joke560.html'


class Joke561(JokePage):
    template_name = 'my_simple_survey/Joke561.html'


class Joke562(JokePage):
    template_name = 'my_simple_survey/Joke562.html'


class Joke563(JokePage):
    template_name = 'my_simple_survey/Joke563.html'


class Joke564(JokePage):
    template_name = 'my_simple_survey/Joke564.html'


class Joke565(JokePage):
    template_name = 'my_simple_survey/Joke565.html'


class Joke566(JokePage):
    template_name = 'my_simple_survey/Joke566.html'


class Joke567(JokePage):
    template_name = 'my_simple_survey/Joke567.html'


class Joke568(JokePage):
    template_name = 'my_simple_survey/Joke568.html'


class Joke569(JokePage):
    template_name = 'my_simple_survey/Joke569.html'


class Joke570(JokePage):
    template_name = 'my_simple_survey/Joke570.html'


class Joke571(JokePage):
    template_name = 'my_simple_survey/Joke571.html'


class Joke572(JokePage):
    template_name = 'my_simple_survey/Joke572.html'


class Joke573(JokePage):
    template_name = 'my_simple_survey/Joke573.html'


class Joke574(JokePage):
    template_name = 'my_simple_survey/Joke574.html'


class Joke575(JokePage):
    template_name = 'my_simple_survey/Joke575.html'


class Joke576(JokePage):
    template_name = 'my_simple_survey/Joke576.html'


class Joke577(JokePage):
    template_name = 'my_simple_survey/Joke577.html'


class Joke578(JokePage):
    template_name = 'my_simple_survey/Joke578.html'


class Joke579(JokePage):
    template_name = 'my_simple_survey/Joke579.html'


class Joke580(JokePage):
    template_name = 'my_simple_survey/Joke580.html'


class Joke581(JokePage):
    template_name = 'my_simple_survey/Joke581.html'


class Joke582(JokePage):
    template_name = 'my_simple_survey/Joke582.html'


class Joke583(JokePage):
    template_name = 'my_simple_survey/Joke583.html'


class Joke584(JokePage):
    template_name = 'my_simple_survey/Joke584.html'


class Joke585(JokePage):
    template_name = 'my_simple_survey/Joke585.html'


class Joke586(JokePage):
    template_name = 'my_simple_survey/Joke586.html'


class Joke587(JokePage):
    template_name = 'my_simple_survey/Joke587.html'


class Joke588(JokePage):
    template_name = 'my_simple_survey/Joke588.html'


class Joke589(JokePage):
    template_name = 'my_simple_survey/Joke589.html'


class Joke590(JokePage):
    template_name = 'my_simple_survey/Joke590.html'


class Joke591(JokePage):
    template_name = 'my_simple_survey/Joke591.html'


class Joke592(JokePage):
    template_name = 'my_simple_survey/Joke592.html'


class Joke593(JokePage):
    template_name = 'my_simple_survey/Joke593.html'


class Joke594(JokePage):
    template_name = 'my_simple_survey/Joke594.html'


class Joke595(JokePage):
    template_name = 'my_simple_survey/Joke595.html'


class Joke596(JokePage):
    template_name = 'my_simple_survey/Joke596.html'


class Joke597(JokePage):
    template_name = 'my_simple_survey/Joke597.html'


class Joke598(JokePage):
    template_name = 'my_simple_survey/Joke598.html'


class Joke599(JokePage):
    template_name = 'my_simple_survey/Joke599.html'


class Joke600(JokePage):
    template_name = 'my_simple_survey/Joke600.html'


class Joke601(JokePage):
    template_name = 'my_simple_survey/Joke601.html'


class Joke602(JokePage):
    template_name = 'my_simple_survey/Joke602.html'


class Joke603(JokePage):
    template_name = 'my_simple_survey/Joke603.html'


class Joke604(JokePage):
    template_name = 'my_simple_survey/Joke604.html'


class Joke605(JokePage):
    template_name = 'my_simple_survey/Joke605.html'


class Joke606(JokePage):
    template_name = 'my_simple_survey/Joke606.html'


class Joke607(JokePage):
    template_name = 'my_simple_survey/Joke607.html'


class Joke608(JokePage):
    template_name = 'my_simple_survey/Joke608.html'


class Joke609(JokePage):
    template_name = 'my_simple_survey/Joke609.html'


class Joke610(JokePage):
    template_name = 'my_simple_survey/Joke610.html'


class Joke611(JokePage):
    template_name = 'my_simple_survey/Joke611.html'


class Joke612(JokePage):
    template_name = 'my_simple_survey/Joke612.html'


class Joke613(JokePage):
    template_name = 'my_simple_survey/Joke613.html'


class Joke614(JokePage):
    template_name = 'my_simple_survey/Joke614.html'


class Joke615(JokePage):
    template_name = 'my_simple_survey/Joke615.html'


class Joke616(JokePage):
    template_name = 'my_simple_survey/Joke616.html'


class Joke617(JokePage):
    template_name = 'my_simple_survey/Joke617.html'


class Joke618(JokePage):
    template_name = 'my_simple_survey/Joke618.html'


class Joke619(JokePage):
    template_name = 'my_simple_survey/Joke619.html'


class Joke620(JokePage):
    template_name = 'my_simple_survey/Joke620.html'


class Joke621(JokePage):
    template_name = 'my_simple_survey/Joke621.html'


class Joke622(JokePage):
    template_name = 'my_simple_survey/Joke622.html'


class Joke623(JokePage):
    template_name = 'my_simple_survey/Joke623.html'


class Joke624(JokePage):
    template_name = 'my_simple_survey/Joke624.html'


class Joke625(JokePage):
    template_name = 'my_simple_survey/Joke625.html'


class Joke626(JokePage):
    template_name = 'my_simple_survey/Joke626.html'


class Joke627(JokePage):
    template_name = 'my_simple_survey/Joke627.html'


class Joke628(JokePage):
    template_name = 'my_simple_survey/Joke628.html'


class Joke629(JokePage):
    template_name = 'my_simple_survey/Joke629.html'


class Joke630(JokePage):
    template_name = 'my_simple_survey/Joke630.html'


class Joke631(JokePage):
    template_name = 'my_simple_survey/Joke631.html'


class Joke632(JokePage):
    template_name = 'my_simple_survey/Joke632.html'


class Joke633(JokePage):
    template_name = 'my_simple_survey/Joke633.html'


class Joke634(JokePage):
    template_name = 'my_simple_survey/Joke634.html'


class Joke635(JokePage):
    template_name = 'my_simple_survey/Joke635.html'


class Joke636(JokePage):
    template_name = 'my_simple_survey/Joke636.html'


class Joke637(JokePage):
    template_name = 'my_simple_survey/Joke637.html'


class Joke638(JokePage):
    template_name = 'my_simple_survey/Joke638.html'


class Joke639(JokePage):
    template_name = 'my_simple_survey/Joke639.html'


class Joke640(JokePage):
    template_name = 'my_simple_survey/Joke640.html'


class Joke641(JokePage):
    template_name = 'my_simple_survey/Joke641.html'


class Joke642(JokePage):
    template_name = 'my_simple_survey/Joke642.html'


class Joke643(JokePage):
    template_name = 'my_simple_survey/Joke643.html'


class Joke644(JokePage):
    template_name = 'my_simple_survey/Joke644.html'


class Joke645(JokePage):
    template_name = 'my_simple_survey/Joke645.html'


class Joke646(JokePage):
    template_name = 'my_simple_survey/Joke646.html'


class Joke647(JokePage):
    template_name = 'my_simple_survey/Joke647.html'


class Joke648(JokePage):
    template_name = 'my_simple_survey/Joke648.html'


class Joke649(JokePage):
    template_name = 'my_simple_survey/Joke649.html'


class Joke650(JokePage):
    template_name = 'my_simple_survey/Joke650.html'


class Joke651(JokePage):
    template_name = 'my_simple_survey/Joke651.html'


class Joke652(JokePage):
    template_name = 'my_simple_survey/Joke652.html'


class Joke653(JokePage):
    template_name = 'my_simple_survey/Joke653.html'


class Joke654(JokePage):
    template_name = 'my_simple_survey/Joke654.html'


class Joke655(JokePage):
    template_name = 'my_simple_survey/Joke655.html'


class Joke656(JokePage):
    template_name = 'my_simple_survey/Joke656.html'


class Joke657(JokePage):
    template_name = 'my_simple_survey/Joke657.html'


class Joke658(JokePage):
    template_name = 'my_simple_survey/Joke658.html'


class Joke659(JokePage):
    template_name = 'my_simple_survey/Joke659.html'


class Joke660(JokePage):
    template_name = 'my_simple_survey/Joke660.html'


class Joke661(JokePage):
    template_name = 'my_simple_survey/Joke661.html'


class Joke662(JokePage):
    template_name = 'my_simple_survey/Joke662.html'


class Joke663(JokePage):
    template_name = 'my_simple_survey/Joke663.html'


class Joke664(JokePage):
    template_name = 'my_simple_survey/Joke664.html'


class Joke665(JokePage):
    template_name = 'my_simple_survey/Joke665.html'


class Joke666(JokePage):
    template_name = 'my_simple_survey/Joke666.html'


class Joke667(JokePage):
    template_name = 'my_simple_survey/Joke667.html'


class Joke668(JokePage):
    template_name = 'my_simple_survey/Joke668.html'


class Joke669(JokePage):
    template_name = 'my_simple_survey/Joke669.html'


class Joke670(JokePage):
    template_name = 'my_simple_survey/Joke670.html'


class Joke671(JokePage):
    template_name = 'my_simple_survey/Joke671.html'


class Joke672(JokePage):
    template_name = 'my_simple_survey/Joke672.html'


class Joke673(JokePage):
    template_name = 'my_simple_survey/Joke673.html'


class Joke674(JokePage):
    template_name = 'my_simple_survey/Joke674.html'


class Joke675(JokePage):
    template_name = 'my_simple_survey/Joke675.html'


class Joke676(JokePage):
    template_name = 'my_simple_survey/Joke676.html'


class Joke677(JokePage):
    template_name = 'my_simple_survey/Joke677.html'


class Joke678(JokePage):
    template_name = 'my_simple_survey/Joke678.html'


class Joke679(JokePage):
    template_name = 'my_simple_survey/Joke679.html'


class Joke680(JokePage):
    template_name = 'my_simple_survey/Joke680.html'


class Joke681(JokePage):
    template_name = 'my_simple_survey/Joke681.html'


class Joke682(JokePage):
    template_name = 'my_simple_survey/Joke682.html'


class Joke683(JokePage):
    template_name = 'my_simple_survey/Joke683.html'


class Joke684(JokePage):
    template_name = 'my_simple_survey/Joke684.html'


class Joke685(JokePage):
    template_name = 'my_simple_survey/Joke685.html'


class Joke686(JokePage):
    template_name = 'my_simple_survey/Joke686.html'


class Joke687(JokePage):
    template_name = 'my_simple_survey/Joke687.html'


class Joke688(JokePage):
    template_name = 'my_simple_survey/Joke688.html'


class Joke689(JokePage):
    template_name = 'my_simple_survey/Joke689.html'


class Joke690(JokePage):
    template_name = 'my_simple_survey/Joke690.html'


class Joke691(JokePage):
    template_name = 'my_simple_survey/Joke691.html'


class Joke692(JokePage):
    template_name = 'my_simple_survey/Joke692.html'


class Joke693(JokePage):
    template_name = 'my_simple_survey/Joke693.html'


class Joke694(JokePage):
    template_name = 'my_simple_survey/Joke694.html'


class Joke695(JokePage):
    template_name = 'my_simple_survey/Joke695.html'


class Joke696(JokePage):
    template_name = 'my_simple_survey/Joke696.html'


class Joke697(JokePage):
    template_name = 'my_simple_survey/Joke697.html'


class Joke698(JokePage):
    template_name = 'my_simple_survey/Joke698.html'


class Joke699(JokePage):
    template_name = 'my_simple_survey/Joke699.html'


class Joke700(JokePage):
    template_name = 'my_simple_survey/Joke700.html'


class Joke701(JokePage):
    template_name = 'my_simple_survey/Joke701.html'


class Joke702(JokePage):
    template_name = 'my_simple_survey/Joke702.html'


class Joke703(JokePage):
    template_name = 'my_simple_survey/Joke703.html'


class Joke704(JokePage):
    template_name = 'my_simple_survey/Joke704.html'


class Joke705(JokePage):
    template_name = 'my_simple_survey/Joke705.html'


class Joke706(JokePage):
    template_name = 'my_simple_survey/Joke706.html'


class Joke707(JokePage):
    template_name = 'my_simple_survey/Joke707.html'


class Joke708(JokePage):
    template_name = 'my_simple_survey/Joke708.html'


class Joke709(JokePage):
    template_name = 'my_simple_survey/Joke709.html'


class Joke710(JokePage):
    template_name = 'my_simple_survey/Joke710.html'


class Joke711(JokePage):
    template_name = 'my_simple_survey/Joke711.html'


class Joke712(JokePage):
    template_name = 'my_simple_survey/Joke712.html'


class Joke713(JokePage):
    template_name = 'my_simple_survey/Joke713.html'


class Joke714(JokePage):
    template_name = 'my_simple_survey/Joke714.html'


class Joke715(JokePage):
    template_name = 'my_simple_survey/Joke715.html'


class Joke716(JokePage):
    template_name = 'my_simple_survey/Joke716.html'


class Joke717(JokePage):
    template_name = 'my_simple_survey/Joke717.html'


class Joke718(JokePage):
    template_name = 'my_simple_survey/Joke718.html'


class Joke719(JokePage):
    template_name = 'my_simple_survey/Joke719.html'


class Joke720(JokePage):
    template_name = 'my_simple_survey/Joke720.html'


class Joke721(JokePage):
    template_name = 'my_simple_survey/Joke721.html'


class Joke722(JokePage):
    template_name = 'my_simple_survey/Joke722.html'


class Joke723(JokePage):
    template_name = 'my_simple_survey/Joke723.html'


class Joke724(JokePage):
    template_name = 'my_simple_survey/Joke724.html'


class Joke725(JokePage):
    template_name = 'my_simple_survey/Joke725.html'


class Joke726(JokePage):
    template_name = 'my_simple_survey/Joke726.html'


class Joke727(JokePage):
    template_name = 'my_simple_survey/Joke727.html'


class Joke728(JokePage):
    template_name = 'my_simple_survey/Joke728.html'


class Joke729(JokePage):
    template_name = 'my_simple_survey/Joke729.html'


class Joke730(JokePage):
    template_name = 'my_simple_survey/Joke730.html'


class Joke731(JokePage):
    template_name = 'my_simple_survey/Joke731.html'


class Joke732(JokePage):
    template_name = 'my_simple_survey/Joke732.html'


class Joke733(JokePage):
    template_name = 'my_simple_survey/Joke733.html'


class Joke734(JokePage):
    template_name = 'my_simple_survey/Joke734.html'


class Joke735(JokePage):
    template_name = 'my_simple_survey/Joke735.html'


class Joke736(JokePage):
    template_name = 'my_simple_survey/Joke736.html'


class Joke737(JokePage):
    template_name = 'my_simple_survey/Joke737.html'


class Joke738(JokePage):
    template_name = 'my_simple_survey/Joke738.html'


class Joke739(JokePage):
    template_name = 'my_simple_survey/Joke739.html'


class Joke740(JokePage):
    template_name = 'my_simple_survey/Joke740.html'


class Joke741(JokePage):
    template_name = 'my_simple_survey/Joke741.html'


class Joke742(JokePage):
    template_name = 'my_simple_survey/Joke742.html'


class Joke743(JokePage):
    template_name = 'my_simple_survey/Joke743.html'


class Joke744(JokePage):
    template_name = 'my_simple_survey/Joke744.html'


class Joke745(JokePage):
    template_name = 'my_simple_survey/Joke745.html'


class Joke746(JokePage):
    template_name = 'my_simple_survey/Joke746.html'


class Joke747(JokePage):
    template_name = 'my_simple_survey/Joke747.html'


class Joke748(JokePage):
    template_name = 'my_simple_survey/Joke748.html'


class Joke749(JokePage):
    template_name = 'my_simple_survey/Joke749.html'


class Joke750(JokePage):
    template_name = 'my_simple_survey/Joke750.html'


class Joke751(JokePage):
    template_name = 'my_simple_survey/Joke751.html'


class Joke752(JokePage):
    template_name = 'my_simple_survey/Joke752.html'


class Joke753(JokePage):
    template_name = 'my_simple_survey/Joke753.html'


class Joke754(JokePage):
    template_name = 'my_simple_survey/Joke754.html'


class Joke755(JokePage):
    template_name = 'my_simple_survey/Joke755.html'


class Joke756(JokePage):
    template_name = 'my_simple_survey/Joke756.html'


class Joke757(JokePage):
    template_name = 'my_simple_survey/Joke757.html'


class Joke758(JokePage):
    template_name = 'my_simple_survey/Joke758.html'


class Joke759(JokePage):
    template_name = 'my_simple_survey/Joke759.html'


class Joke760(JokePage):
    template_name = 'my_simple_survey/Joke760.html'


class Joke761(JokePage):
    template_name = 'my_simple_survey/Joke761.html'


class Joke762(JokePage):
    template_name = 'my_simple_survey/Joke762.html'


class Joke763(JokePage):
    template_name = 'my_simple_survey/Joke763.html'


class Joke764(JokePage):
    template_name = 'my_simple_survey/Joke764.html'


class Joke765(JokePage):
    template_name = 'my_simple_survey/Joke765.html'


class Joke766(JokePage):
    template_name = 'my_simple_survey/Joke766.html'


class Joke767(JokePage):
    template_name = 'my_simple_survey/Joke767.html'


class Joke768(JokePage):
    template_name = 'my_simple_survey/Joke768.html'


class Joke769(JokePage):
    template_name = 'my_simple_survey/Joke769.html'


class Joke770(JokePage):
    template_name = 'my_simple_survey/Joke770.html'


class Joke771(JokePage):
    template_name = 'my_simple_survey/Joke771.html'


class Joke772(JokePage):
    template_name = 'my_simple_survey/Joke772.html'


class Joke773(JokePage):
    template_name = 'my_simple_survey/Joke773.html'


class Joke774(JokePage):
    template_name = 'my_simple_survey/Joke774.html'


class Joke775(JokePage):
    template_name = 'my_simple_survey/Joke775.html'


class Joke776(JokePage):
    template_name = 'my_simple_survey/Joke776.html'


class Joke777(JokePage):
    template_name = 'my_simple_survey/Joke777.html'


class Joke778(JokePage):
    template_name = 'my_simple_survey/Joke778.html'


class Joke779(JokePage):
    template_name = 'my_simple_survey/Joke779.html'


class Joke780(JokePage):
    template_name = 'my_simple_survey/Joke780.html'


class Joke781(JokePage):
    template_name = 'my_simple_survey/Joke781.html'


class Joke782(JokePage):
    template_name = 'my_simple_survey/Joke782.html'


class Joke783(JokePage):
    template_name = 'my_simple_survey/Joke783.html'


class Joke784(JokePage):
    template_name = 'my_simple_survey/Joke784.html'


class Joke785(JokePage):
    template_name = 'my_simple_survey/Joke785.html'


class Joke786(JokePage):
    template_name = 'my_simple_survey/Joke786.html'


class Joke787(JokePage):
    template_name = 'my_simple_survey/Joke787.html'


class Joke788(JokePage):
    template_name = 'my_simple_survey/Joke788.html'


class Joke789(JokePage):
    template_name = 'my_simple_survey/Joke789.html'


class Joke790(JokePage):
    template_name = 'my_simple_survey/Joke790.html'


class Joke791(JokePage):
    template_name = 'my_simple_survey/Joke791.html'


class Joke792(JokePage):
    template_name = 'my_simple_survey/Joke792.html'


class Joke793(JokePage):
    template_name = 'my_simple_survey/Joke793.html'


class Joke794(JokePage):
    template_name = 'my_simple_survey/Joke794.html'


class Joke795(JokePage):
    template_name = 'my_simple_survey/Joke795.html'


class Joke796(JokePage):
    template_name = 'my_simple_survey/Joke796.html'


class Joke797(JokePage):
    template_name = 'my_simple_survey/Joke797.html'


class Joke798(JokePage):
    template_name = 'my_simple_survey/Joke798.html'


class Joke799(JokePage):
    template_name = 'my_simple_survey/Joke799.html'


class Joke800(JokePage):
    template_name = 'my_simple_survey/Joke800.html'


class Joke801(JokePage):
    template_name = 'my_simple_survey/Joke801.html'


class Joke802(JokePage):
    template_name = 'my_simple_survey/Joke802.html'


class Joke803(JokePage):
    template_name = 'my_simple_survey/Joke803.html'


class Joke804(JokePage):
    template_name = 'my_simple_survey/Joke804.html'


class Joke805(JokePage):
    template_name = 'my_simple_survey/Joke805.html'


class Joke806(JokePage):
    template_name = 'my_simple_survey/Joke806.html'


class Joke807(JokePage):
    template_name = 'my_simple_survey/Joke807.html'


class Joke808(JokePage):
    template_name = 'my_simple_survey/Joke808.html'


class Joke809(JokePage):
    template_name = 'my_simple_survey/Joke809.html'


class Joke810(JokePage):
    template_name = 'my_simple_survey/Joke810.html'


class Joke811(JokePage):
    template_name = 'my_simple_survey/Joke811.html'


class Joke812(JokePage):
    template_name = 'my_simple_survey/Joke812.html'


class Joke813(JokePage):
    template_name = 'my_simple_survey/Joke813.html'


class Joke814(JokePage):
    template_name = 'my_simple_survey/Joke814.html'


class Joke815(JokePage):
    template_name = 'my_simple_survey/Joke815.html'


class Joke816(JokePage):
    template_name = 'my_simple_survey/Joke816.html'


class Joke817(JokePage):
    template_name = 'my_simple_survey/Joke817.html'


class Joke818(JokePage):
    template_name = 'my_simple_survey/Joke818.html'


class Joke819(JokePage):
    template_name = 'my_simple_survey/Joke819.html'


class Joke820(JokePage):
    template_name = 'my_simple_survey/Joke820.html'


class Joke821(JokePage):
    template_name = 'my_simple_survey/Joke821.html'


class Joke822(JokePage):
    template_name = 'my_simple_survey/Joke822.html'


class Joke823(JokePage):
    template_name = 'my_simple_survey/Joke823.html'


class Joke824(JokePage):
    template_name = 'my_simple_survey/Joke824.html'


class Joke825(JokePage):
    template_name = 'my_simple_survey/Joke825.html'


class Joke826(JokePage):
    template_name = 'my_simple_survey/Joke826.html'


class Joke827(JokePage):
    template_name = 'my_simple_survey/Joke827.html'


class Joke828(JokePage):
    template_name = 'my_simple_survey/Joke828.html'


class Joke829(JokePage):
    template_name = 'my_simple_survey/Joke829.html'


class Joke830(JokePage):
    template_name = 'my_simple_survey/Joke830.html'


class Joke831(JokePage):
    template_name = 'my_simple_survey/Joke831.html'


class Joke832(JokePage):
    template_name = 'my_simple_survey/Joke832.html'


class Joke833(JokePage):
    template_name = 'my_simple_survey/Joke833.html'


class Joke834(JokePage):
    template_name = 'my_simple_survey/Joke834.html'


class Joke835(JokePage):
    template_name = 'my_simple_survey/Joke835.html'


class Joke836(JokePage):
    template_name = 'my_simple_survey/Joke836.html'


class Joke837(JokePage):
    template_name = 'my_simple_survey/Joke837.html'


class Joke838(JokePage):
    template_name = 'my_simple_survey/Joke838.html'


class Joke839(JokePage):
    template_name = 'my_simple_survey/Joke839.html'


class Joke840(JokePage):
    template_name = 'my_simple_survey/Joke840.html'


class Joke841(JokePage):
    template_name = 'my_simple_survey/Joke841.html'


class Joke842(JokePage):
    template_name = 'my_simple_survey/Joke842.html'


class Joke843(JokePage):
    template_name = 'my_simple_survey/Joke843.html'


class Joke844(JokePage):
    template_name = 'my_simple_survey/Joke844.html'


class Joke845(JokePage):
    template_name = 'my_simple_survey/Joke845.html'


class Joke846(JokePage):
    template_name = 'my_simple_survey/Joke846.html'


class Joke847(JokePage):
    template_name = 'my_simple_survey/Joke847.html'


class Joke848(JokePage):
    template_name = 'my_simple_survey/Joke848.html'


class Joke849(JokePage):
    template_name = 'my_simple_survey/Joke849.html'


class Joke850(JokePage):
    template_name = 'my_simple_survey/Joke850.html'


class Joke851(JokePage):
    template_name = 'my_simple_survey/Joke851.html'


class Joke852(JokePage):
    template_name = 'my_simple_survey/Joke852.html'


class Joke853(JokePage):
    template_name = 'my_simple_survey/Joke853.html'


class Joke854(JokePage):
    template_name = 'my_simple_survey/Joke854.html'


class Joke855(JokePage):
    template_name = 'my_simple_survey/Joke855.html'


class Joke856(JokePage):
    template_name = 'my_simple_survey/Joke856.html'


class Joke857(JokePage):
    template_name = 'my_simple_survey/Joke857.html'


class Joke858(JokePage):
    template_name = 'my_simple_survey/Joke858.html'


class Joke859(JokePage):
    template_name = 'my_simple_survey/Joke859.html'


class Joke860(JokePage):
    template_name = 'my_simple_survey/Joke860.html'


class Joke861(JokePage):
    template_name = 'my_simple_survey/Joke861.html'


class Joke862(JokePage):
    template_name = 'my_simple_survey/Joke862.html'


class Joke863(JokePage):
    template_name = 'my_simple_survey/Joke863.html'


class Joke864(JokePage):
    template_name = 'my_simple_survey/Joke864.html'


class Joke865(JokePage):
    template_name = 'my_simple_survey/Joke865.html'


class Joke866(JokePage):
    template_name = 'my_simple_survey/Joke866.html'


class Joke867(JokePage):
    template_name = 'my_simple_survey/Joke867.html'


class Joke868(JokePage):
    template_name = 'my_simple_survey/Joke868.html'


class Joke869(JokePage):
    template_name = 'my_simple_survey/Joke869.html'


class Joke870(JokePage):
    template_name = 'my_simple_survey/Joke870.html'


class Joke871(JokePage):
    template_name = 'my_simple_survey/Joke871.html'


class Joke872(JokePage):
    template_name = 'my_simple_survey/Joke872.html'


class Joke873(JokePage):
    template_name = 'my_simple_survey/Joke873.html'


class Joke874(JokePage):
    template_name = 'my_simple_survey/Joke874.html'


class Joke875(JokePage):
    template_name = 'my_simple_survey/Joke875.html'


class Joke876(JokePage):
    template_name = 'my_simple_survey/Joke876.html'


class Joke877(JokePage):
    template_name = 'my_simple_survey/Joke877.html'


class Joke878(JokePage):
    template_name = 'my_simple_survey/Joke878.html'


class Joke879(JokePage):
    template_name = 'my_simple_survey/Joke879.html'


class Joke880(JokePage):
    template_name = 'my_simple_survey/Joke880.html'


class Joke881(JokePage):
    template_name = 'my_simple_survey/Joke881.html'


class Joke882(JokePage):
    template_name = 'my_simple_survey/Joke882.html'


class Joke883(JokePage):
    template_name = 'my_simple_survey/Joke883.html'


class Joke884(JokePage):
    template_name = 'my_simple_survey/Joke884.html'


class Joke885(JokePage):
    template_name = 'my_simple_survey/Joke885.html'


class Joke886(JokePage):
    template_name = 'my_simple_survey/Joke886.html'


class Joke887(JokePage):
    template_name = 'my_simple_survey/Joke887.html'


class Joke888(JokePage):
    template_name = 'my_simple_survey/Joke888.html'


class Joke889(JokePage):
    template_name = 'my_simple_survey/Joke889.html'


class Joke890(JokePage):
    template_name = 'my_simple_survey/Joke890.html'


class Joke891(JokePage):
    template_name = 'my_simple_survey/Joke891.html'


class Joke892(JokePage):
    template_name = 'my_simple_survey/Joke892.html'


class Joke893(JokePage):
    template_name = 'my_simple_survey/Joke893.html'


class Joke894(JokePage):
    template_name = 'my_simple_survey/Joke894.html'


class Joke895(JokePage):
    template_name = 'my_simple_survey/Joke895.html'


class Joke896(JokePage):
    template_name = 'my_simple_survey/Joke896.html'


class Joke897(JokePage):
    template_name = 'my_simple_survey/Joke897.html'


class Joke898(JokePage):
    template_name = 'my_simple_survey/Joke898.html'


class Joke899(JokePage):
    template_name = 'my_simple_survey/Joke899.html'


class Joke900(JokePage):
    template_name = 'my_simple_survey/Joke900.html'


class Joke901(JokePage):
    template_name = 'my_simple_survey/Joke901.html'


class Joke902(JokePage):
    template_name = 'my_simple_survey/Joke902.html'


class Joke903(JokePage):
    template_name = 'my_simple_survey/Joke903.html'


class Joke904(JokePage):
    template_name = 'my_simple_survey/Joke904.html'


class Joke905(JokePage):
    template_name = 'my_simple_survey/Joke905.html'


class Joke906(JokePage):
    template_name = 'my_simple_survey/Joke906.html'


class Joke907(JokePage):
    template_name = 'my_simple_survey/Joke907.html'


class Joke908(JokePage):
    template_name = 'my_simple_survey/Joke908.html'


class Joke909(JokePage):
    template_name = 'my_simple_survey/Joke909.html'


class Joke910(JokePage):
    template_name = 'my_simple_survey/Joke910.html'


class Joke911(JokePage):
    template_name = 'my_simple_survey/Joke911.html'


class Joke912(JokePage):
    template_name = 'my_simple_survey/Joke912.html'


class Joke913(JokePage):
    template_name = 'my_simple_survey/Joke913.html'


class Joke914(JokePage):
    template_name = 'my_simple_survey/Joke914.html'


class Joke915(JokePage):
    template_name = 'my_simple_survey/Joke915.html'


class Joke916(JokePage):
    template_name = 'my_simple_survey/Joke916.html'


class Joke917(JokePage):
    template_name = 'my_simple_survey/Joke917.html'


class Joke918(JokePage):
    template_name = 'my_simple_survey/Joke918.html'


class Joke919(JokePage):
    template_name = 'my_simple_survey/Joke919.html'


class Joke920(JokePage):
    template_name = 'my_simple_survey/Joke920.html'


class Joke921(JokePage):
    template_name = 'my_simple_survey/Joke921.html'


class Joke922(JokePage):
    template_name = 'my_simple_survey/Joke922.html'


class Joke923(JokePage):
    template_name = 'my_simple_survey/Joke923.html'


class Joke924(JokePage):
    template_name = 'my_simple_survey/Joke924.html'


class Joke925(JokePage):
    template_name = 'my_simple_survey/Joke925.html'


class Joke926(JokePage):
    template_name = 'my_simple_survey/Joke926.html'


class Joke927(JokePage):
    template_name = 'my_simple_survey/Joke927.html'


class Joke928(JokePage):
    template_name = 'my_simple_survey/Joke928.html'


class Joke929(JokePage):
    template_name = 'my_simple_survey/Joke929.html'


class Joke930(JokePage):
    template_name = 'my_simple_survey/Joke930.html'


class Joke931(JokePage):
    template_name = 'my_simple_survey/Joke931.html'


class Joke932(JokePage):
    template_name = 'my_simple_survey/Joke932.html'


class Joke933(JokePage):
    template_name = 'my_simple_survey/Joke933.html'


class Joke934(JokePage):
    template_name = 'my_simple_survey/Joke934.html'


class Joke935(JokePage):
    template_name = 'my_simple_survey/Joke935.html'


class Joke936(JokePage):
    template_name = 'my_simple_survey/Joke936.html'


class Joke937(JokePage):
    template_name = 'my_simple_survey/Joke937.html'


class Joke938(JokePage):
    template_name = 'my_simple_survey/Joke938.html'


class Joke939(JokePage):
    template_name = 'my_simple_survey/Joke939.html'


class Joke940(JokePage):
    template_name = 'my_simple_survey/Joke940.html'


class Joke941(JokePage):
    template_name = 'my_simple_survey/Joke941.html'


class Joke942(JokePage):
    template_name = 'my_simple_survey/Joke942.html'


class Joke943(JokePage):
    template_name = 'my_simple_survey/Joke943.html'


class Joke944(JokePage):
    template_name = 'my_simple_survey/Joke944.html'


class Joke945(JokePage):
    template_name = 'my_simple_survey/Joke945.html'


class Joke946(JokePage):
    template_name = 'my_simple_survey/Joke946.html'


class Joke947(JokePage):
    template_name = 'my_simple_survey/Joke947.html'


class Joke948(JokePage):
    template_name = 'my_simple_survey/Joke948.html'


class Joke949(JokePage):
    template_name = 'my_simple_survey/Joke949.html'


class Joke950(JokePage):
    template_name = 'my_simple_survey/Joke950.html'


class Joke951(JokePage):
    template_name = 'my_simple_survey/Joke951.html'


class Joke952(JokePage):
    template_name = 'my_simple_survey/Joke952.html'


class Joke953(JokePage):
    template_name = 'my_simple_survey/Joke953.html'


class Joke954(JokePage):
    template_name = 'my_simple_survey/Joke954.html'


class Joke955(JokePage):
    template_name = 'my_simple_survey/Joke955.html'


class Joke956(JokePage):
    template_name = 'my_simple_survey/Joke956.html'


class Joke957(JokePage):
    template_name = 'my_simple_survey/Joke957.html'


class Joke958(JokePage):
    template_name = 'my_simple_survey/Joke958.html'


class Joke959(JokePage):
    template_name = 'my_simple_survey/Joke959.html'


class Joke960(JokePage):
    template_name = 'my_simple_survey/Joke960.html'


class Joke961(JokePage):
    template_name = 'my_simple_survey/Joke961.html'


class Joke962(JokePage):
    template_name = 'my_simple_survey/Joke962.html'


class Joke963(JokePage):
    template_name = 'my_simple_survey/Joke963.html'


class Joke964(JokePage):
    template_name = 'my_simple_survey/Joke964.html'


class Joke965(JokePage):
    template_name = 'my_simple_survey/Joke965.html'


class Joke966(JokePage):
    template_name = 'my_simple_survey/Joke966.html'


class Joke967(JokePage):
    template_name = 'my_simple_survey/Joke967.html'


class Joke968(JokePage):
    template_name = 'my_simple_survey/Joke968.html'


class Joke969(JokePage):
    template_name = 'my_simple_survey/Joke969.html'


class Joke970(JokePage):
    template_name = 'my_simple_survey/Joke970.html'


class Joke971(JokePage):
    template_name = 'my_simple_survey/Joke971.html'


class Joke972(JokePage):
    template_name = 'my_simple_survey/Joke972.html'


class Joke973(JokePage):
    template_name = 'my_simple_survey/Joke973.html'


class Joke974(JokePage):
    template_name = 'my_simple_survey/Joke974.html'


class Joke975(JokePage):
    template_name = 'my_simple_survey/Joke975.html'


class Joke976(JokePage):
    template_name = 'my_simple_survey/Joke976.html'


class Joke977(JokePage):
    template_name = 'my_simple_survey/Joke977.html'


class Joke978(JokePage):
    template_name = 'my_simple_survey/Joke978.html'


class Joke979(JokePage):
    template_name = 'my_simple_survey/Joke979.html'


class Joke980(JokePage):
    template_name = 'my_simple_survey/Joke980.html'


class Joke981(JokePage):
    template_name = 'my_simple_survey/Joke981.html'


class Joke982(JokePage):
    template_name = 'my_simple_survey/Joke982.html'


class Joke983(JokePage):
    template_name = 'my_simple_survey/Joke983.html'


class Joke984(JokePage):
    template_name = 'my_simple_survey/Joke984.html'


class Joke985(JokePage):
    template_name = 'my_simple_survey/Joke985.html'


class Joke986(JokePage):
    template_name = 'my_simple_survey/Joke986.html'


class Joke987(JokePage):
    template_name = 'my_simple_survey/Joke987.html'


class Joke988(JokePage):
    template_name = 'my_simple_survey/Joke988.html'


class Joke989(JokePage):
    template_name = 'my_simple_survey/Joke989.html'


class Joke990(JokePage):
    template_name = 'my_simple_survey/Joke990.html'


class Joke991(JokePage):
    template_name = 'my_simple_survey/Joke991.html'


class Joke992(JokePage):
    template_name = 'my_simple_survey/Joke992.html'


class Joke993(JokePage):
    template_name = 'my_simple_survey/Joke993.html'


class Joke994(JokePage):
    template_name = 'my_simple_survey/Joke994.html'


class Joke995(JokePage):
    template_name = 'my_simple_survey/Joke995.html'


class Joke996(JokePage):
    template_name = 'my_simple_survey/Joke996.html'


class Joke997(JokePage):
    template_name = 'my_simple_survey/Joke997.html'


class Joke998(JokePage):
    template_name = 'my_simple_survey/Joke998.html'


class Joke999(JokePage):
    template_name = 'my_simple_survey/Joke999.html'


class Joke1000(JokePage):
    template_name = 'my_simple_survey/Joke1000.html'


class Joke1001(JokePage):
    template_name = 'my_simple_survey/Joke1001.html'


class Joke1002(JokePage):
    template_name = 'my_simple_survey/Joke1002.html'


class Joke1003(JokePage):
    template_name = 'my_simple_survey/Joke1003.html'


class Joke1004(JokePage):
    template_name = 'my_simple_survey/Joke1004.html'


class Joke1005(JokePage):
    template_name = 'my_simple_survey/Joke1005.html'


class Joke1006(JokePage):
    template_name = 'my_simple_survey/Joke1006.html'


class Joke1007(JokePage):
    template_name = 'my_simple_survey/Joke1007.html'


class Joke1008(JokePage):
    template_name = 'my_simple_survey/Joke1008.html'


class Joke1009(JokePage):
    template_name = 'my_simple_survey/Joke1009.html'


class Joke1010(JokePage):
    template_name = 'my_simple_survey/Joke1010.html'


class Joke1011(JokePage):
    template_name = 'my_simple_survey/Joke1011.html'


class Joke1012(JokePage):
    template_name = 'my_simple_survey/Joke1012.html'


class Joke1013(JokePage):
    template_name = 'my_simple_survey/Joke1013.html'


class Joke1014(JokePage):
    template_name = 'my_simple_survey/Joke1014.html'


class Joke1015(JokePage):
    template_name = 'my_simple_survey/Joke1015.html'


class Joke1016(JokePage):
    template_name = 'my_simple_survey/Joke1016.html'


class Joke1017(JokePage):
    template_name = 'my_simple_survey/Joke1017.html'


class Joke1018(JokePage):
    template_name = 'my_simple_survey/Joke1018.html'


class Joke1019(JokePage):
    template_name = 'my_simple_survey/Joke1019.html'


class Joke1020(JokePage):
    template_name = 'my_simple_survey/Joke1020.html'


class Joke1021(JokePage):
    template_name = 'my_simple_survey/Joke1021.html'


class Joke1022(JokePage):
    template_name = 'my_simple_survey/Joke1022.html'


class Joke1023(JokePage):
    template_name = 'my_simple_survey/Joke1023.html'


class Joke1024(JokePage):
    template_name = 'my_simple_survey/Joke1024.html'


class Joke1025(JokePage):
    template_name = 'my_simple_survey/Joke1025.html'


class Joke1026(JokePage):
    template_name = 'my_simple_survey/Joke1026.html'


class Joke1027(JokePage):
    template_name = 'my_simple_survey/Joke1027.html'


class Joke1028(JokePage):
    template_name = 'my_simple_survey/Joke1028.html'


class Joke1029(JokePage):
    template_name = 'my_simple_survey/Joke1029.html'


class Joke1030(JokePage):
    template_name = 'my_simple_survey/Joke1030.html'


class Joke1031(JokePage):
    template_name = 'my_simple_survey/Joke1031.html'


class Joke1032(JokePage):
    template_name = 'my_simple_survey/Joke1032.html'


class Joke1033(JokePage):
    template_name = 'my_simple_survey/Joke1033.html'


class Joke1034(JokePage):
    template_name = 'my_simple_survey/Joke1034.html'


class Joke1035(JokePage):
    template_name = 'my_simple_survey/Joke1035.html'


class Joke1036(JokePage):
    template_name = 'my_simple_survey/Joke1036.html'


class Joke1037(JokePage):
    template_name = 'my_simple_survey/Joke1037.html'


class Joke1038(JokePage):
    template_name = 'my_simple_survey/Joke1038.html'


class Joke1039(JokePage):
    template_name = 'my_simple_survey/Joke1039.html'


class Joke1040(JokePage):
    template_name = 'my_simple_survey/Joke1040.html'


class Joke1041(JokePage):
    template_name = 'my_simple_survey/Joke1041.html'


class Joke1042(JokePage):
    template_name = 'my_simple_survey/Joke1042.html'


class Joke1043(JokePage):
    template_name = 'my_simple_survey/Joke1043.html'


class Joke1044(JokePage):
    template_name = 'my_simple_survey/Joke1044.html'


class Joke1045(JokePage):
    template_name = 'my_simple_survey/Joke1045.html'


class Joke1046(JokePage):
    template_name = 'my_simple_survey/Joke1046.html'


class Joke1047(JokePage):
    template_name = 'my_simple_survey/Joke1047.html'


class Joke1048(JokePage):
    template_name = 'my_simple_survey/Joke1048.html'


class Joke1049(JokePage):
    template_name = 'my_simple_survey/Joke1049.html'


class Joke1050(JokePage):
    template_name = 'my_simple_survey/Joke1050.html'


class Joke1051(JokePage):
    template_name = 'my_simple_survey/Joke1051.html'


class Joke1052(JokePage):
    template_name = 'my_simple_survey/Joke1052.html'


class Joke1053(JokePage):
    template_name = 'my_simple_survey/Joke1053.html'


class Joke1054(JokePage):
    template_name = 'my_simple_survey/Joke1054.html'


class Joke1055(JokePage):
    template_name = 'my_simple_survey/Joke1055.html'


class Joke1056(JokePage):
    template_name = 'my_simple_survey/Joke1056.html'


class Joke1057(JokePage):
    template_name = 'my_simple_survey/Joke1057.html'


class Joke1058(JokePage):
    template_name = 'my_simple_survey/Joke1058.html'


class Joke1059(JokePage):
    template_name = 'my_simple_survey/Joke1059.html'


class Joke1060(JokePage):
    template_name = 'my_simple_survey/Joke1060.html'


class Joke1061(JokePage):
    template_name = 'my_simple_survey/Joke1061.html'


class Joke1062(JokePage):
    template_name = 'my_simple_survey/Joke1062.html'


class Joke1063(JokePage):
    template_name = 'my_simple_survey/Joke1063.html'


class Joke1064(JokePage):
    template_name = 'my_simple_survey/Joke1064.html'


class Joke1065(JokePage):
    template_name = 'my_simple_survey/Joke1065.html'


class Joke1066(JokePage):
    template_name = 'my_simple_survey/Joke1066.html'


class Joke1067(JokePage):
    template_name = 'my_simple_survey/Joke1067.html'


class Joke1068(JokePage):
    template_name = 'my_simple_survey/Joke1068.html'


class Joke1069(JokePage):
    template_name = 'my_simple_survey/Joke1069.html'


class Joke1070(JokePage):
    template_name = 'my_simple_survey/Joke1070.html'


class Joke1071(JokePage):
    template_name = 'my_simple_survey/Joke1071.html'


class Joke1072(JokePage):
    template_name = 'my_simple_survey/Joke1072.html'


class Joke1073(JokePage):
    template_name = 'my_simple_survey/Joke1073.html'


class Joke1074(JokePage):
    template_name = 'my_simple_survey/Joke1074.html'


class Joke1075(JokePage):
    template_name = 'my_simple_survey/Joke1075.html'


class Joke1076(JokePage):
    template_name = 'my_simple_survey/Joke1076.html'


class Joke1077(JokePage):
    template_name = 'my_simple_survey/Joke1077.html'


class Joke1078(JokePage):
    template_name = 'my_simple_survey/Joke1078.html'


class Joke1079(JokePage):
    template_name = 'my_simple_survey/Joke1079.html'


class Joke1080(JokePage):
    template_name = 'my_simple_survey/Joke1080.html'


class Joke1081(JokePage):
    template_name = 'my_simple_survey/Joke1081.html'


class Joke1082(JokePage):
    template_name = 'my_simple_survey/Joke1082.html'


class Joke1083(JokePage):
    template_name = 'my_simple_survey/Joke1083.html'


class Joke1084(JokePage):
    template_name = 'my_simple_survey/Joke1084.html'


class Joke1085(JokePage):
    template_name = 'my_simple_survey/Joke1085.html'


class Joke1086(JokePage):
    template_name = 'my_simple_survey/Joke1086.html'


class Joke1087(JokePage):
    template_name = 'my_simple_survey/Joke1087.html'


class Joke1088(JokePage):
    template_name = 'my_simple_survey/Joke1088.html'


class Joke1089(JokePage):
    template_name = 'my_simple_survey/Joke1089.html'


class Joke1090(JokePage):
    template_name = 'my_simple_survey/Joke1090.html'


class Joke1091(JokePage):
    template_name = 'my_simple_survey/Joke1091.html'


class Joke1092(JokePage):
    template_name = 'my_simple_survey/Joke1092.html'


class Joke1093(JokePage):
    template_name = 'my_simple_survey/Joke1093.html'


class Joke1094(JokePage):
    template_name = 'my_simple_survey/Joke1094.html'


class Joke1095(JokePage):
    template_name = 'my_simple_survey/Joke1095.html'


class Joke1096(JokePage):
    template_name = 'my_simple_survey/Joke1096.html'


class Joke1097(JokePage):
    template_name = 'my_simple_survey/Joke1097.html'


class Joke1098(JokePage):
    template_name = 'my_simple_survey/Joke1098.html'


class Joke1099(JokePage):
    template_name = 'my_simple_survey/Joke1099.html'


class Joke1100(JokePage):
    template_name = 'my_simple_survey/Joke1100.html'


class Joke1101(JokePage):
    template_name = 'my_simple_survey/Joke1101.html'


class Joke1102(JokePage):
    template_name = 'my_simple_survey/Joke1102.html'


class Joke1103(JokePage):
    template_name = 'my_simple_survey/Joke1103.html'


class Joke1104(JokePage):
    template_name = 'my_simple_survey/Joke1104.html'


class Joke1105(JokePage):
    template_name = 'my_simple_survey/Joke1105.html'


class Joke1106(JokePage):
    template_name = 'my_simple_survey/Joke1106.html'


class Joke1107(JokePage):
    template_name = 'my_simple_survey/Joke1107.html'


class Joke1108(JokePage):
    template_name = 'my_simple_survey/Joke1108.html'


class Joke1109(JokePage):
    template_name = 'my_simple_survey/Joke1109.html'


class Joke1110(JokePage):
    template_name = 'my_simple_survey/Joke1110.html'


class Joke1111(JokePage):
    template_name = 'my_simple_survey/Joke1111.html'


class Joke1112(JokePage):
    template_name = 'my_simple_survey/Joke1112.html'


class Joke1113(JokePage):
    template_name = 'my_simple_survey/Joke1113.html'


class Joke1114(JokePage):
    template_name = 'my_simple_survey/Joke1114.html'


class Joke1115(JokePage):
    template_name = 'my_simple_survey/Joke1115.html'


class Joke1116(JokePage):
    template_name = 'my_simple_survey/Joke1116.html'


class Joke1117(JokePage):
    template_name = 'my_simple_survey/Joke1117.html'


class Joke1118(JokePage):
    template_name = 'my_simple_survey/Joke1118.html'


class Joke1119(JokePage):
    template_name = 'my_simple_survey/Joke1119.html'


class Joke1120(JokePage):
    template_name = 'my_simple_survey/Joke1120.html'


class Joke1121(JokePage):
    template_name = 'my_simple_survey/Joke1121.html'


class Joke1122(JokePage):
    template_name = 'my_simple_survey/Joke1122.html'


class Joke1123(JokePage):
    template_name = 'my_simple_survey/Joke1123.html'


class Joke1124(JokePage):
    template_name = 'my_simple_survey/Joke1124.html'


class Joke1125(JokePage):
    template_name = 'my_simple_survey/Joke1125.html'


class Joke1126(JokePage):
    template_name = 'my_simple_survey/Joke1126.html'


class Joke1127(JokePage):
    template_name = 'my_simple_survey/Joke1127.html'


class Joke1128(JokePage):
    template_name = 'my_simple_survey/Joke1128.html'


class Joke1129(JokePage):
    template_name = 'my_simple_survey/Joke1129.html'


class Joke1130(JokePage):
    template_name = 'my_simple_survey/Joke1130.html'


class Joke1131(JokePage):
    template_name = 'my_simple_survey/Joke1131.html'


class Joke1132(JokePage):
    template_name = 'my_simple_survey/Joke1132.html'


class Joke1133(JokePage):
    template_name = 'my_simple_survey/Joke1133.html'


class Joke1134(JokePage):
    template_name = 'my_simple_survey/Joke1134.html'


class Joke1135(JokePage):
    template_name = 'my_simple_survey/Joke1135.html'


class Joke1136(JokePage):
    template_name = 'my_simple_survey/Joke1136.html'


class Joke1137(JokePage):
    template_name = 'my_simple_survey/Joke1137.html'


class Joke1138(JokePage):
    template_name = 'my_simple_survey/Joke1138.html'


class Joke1139(JokePage):
    template_name = 'my_simple_survey/Joke1139.html'


class Joke1140(JokePage):
    template_name = 'my_simple_survey/Joke1140.html'


class Joke1141(JokePage):
    template_name = 'my_simple_survey/Joke1141.html'


class Joke1142(JokePage):
    template_name = 'my_simple_survey/Joke1142.html'


class Joke1143(JokePage):
    template_name = 'my_simple_survey/Joke1143.html'


class Joke1144(JokePage):
    template_name = 'my_simple_survey/Joke1144.html'


class Joke1145(JokePage):
    template_name = 'my_simple_survey/Joke1145.html'


class Joke1146(JokePage):
    template_name = 'my_simple_survey/Joke1146.html'


class Joke1147(JokePage):
    template_name = 'my_simple_survey/Joke1147.html'


class Joke1148(JokePage):
    template_name = 'my_simple_survey/Joke1148.html'


class Joke1149(JokePage):
    template_name = 'my_simple_survey/Joke1149.html'


class Joke1150(JokePage):
    template_name = 'my_simple_survey/Joke1150.html'


class Joke1151(JokePage):
    template_name = 'my_simple_survey/Joke1151.html'


class Joke1152(JokePage):
    template_name = 'my_simple_survey/Joke1152.html'


class Joke1153(JokePage):
    template_name = 'my_simple_survey/Joke1153.html'


class Joke1154(JokePage):
    template_name = 'my_simple_survey/Joke1154.html'


class Joke1155(JokePage):
    template_name = 'my_simple_survey/Joke1155.html'


class Joke1156(JokePage):
    template_name = 'my_simple_survey/Joke1156.html'


class Joke1157(JokePage):
    template_name = 'my_simple_survey/Joke1157.html'


class Joke1158(JokePage):
    template_name = 'my_simple_survey/Joke1158.html'


class Joke1159(JokePage):
    template_name = 'my_simple_survey/Joke1159.html'


class Joke1160(JokePage):
    template_name = 'my_simple_survey/Joke1160.html'


class Joke1161(JokePage):
    template_name = 'my_simple_survey/Joke1161.html'


class Joke1162(JokePage):
    template_name = 'my_simple_survey/Joke1162.html'


class Joke1163(JokePage):
    template_name = 'my_simple_survey/Joke1163.html'


class Joke1164(JokePage):
    template_name = 'my_simple_survey/Joke1164.html'


class Joke1165(JokePage):
    template_name = 'my_simple_survey/Joke1165.html'


class Joke1166(JokePage):
    template_name = 'my_simple_survey/Joke1166.html'


class Joke1167(JokePage):
    template_name = 'my_simple_survey/Joke1167.html'


class Joke1168(JokePage):
    template_name = 'my_simple_survey/Joke1168.html'


class Joke1169(JokePage):
    template_name = 'my_simple_survey/Joke1169.html'


class Joke1170(JokePage):
    template_name = 'my_simple_survey/Joke1170.html'


class Joke1171(JokePage):
    template_name = 'my_simple_survey/Joke1171.html'


class Joke1172(JokePage):
    template_name = 'my_simple_survey/Joke1172.html'


class Joke1173(JokePage):
    template_name = 'my_simple_survey/Joke1173.html'


class Joke1174(JokePage):
    template_name = 'my_simple_survey/Joke1174.html'


class Joke1175(JokePage):
    template_name = 'my_simple_survey/Joke1175.html'


class Joke1176(JokePage):
    template_name = 'my_simple_survey/Joke1176.html'


class Joke1177(JokePage):
    template_name = 'my_simple_survey/Joke1177.html'


class Joke1178(JokePage):
    template_name = 'my_simple_survey/Joke1178.html'


class Joke1179(JokePage):
    template_name = 'my_simple_survey/Joke1179.html'


class Joke1180(JokePage):
    template_name = 'my_simple_survey/Joke1180.html'


class Joke1181(JokePage):
    template_name = 'my_simple_survey/Joke1181.html'


class Joke1182(JokePage):
    template_name = 'my_simple_survey/Joke1182.html'


class Joke1183(JokePage):
    template_name = 'my_simple_survey/Joke1183.html'


class Joke1184(JokePage):
    template_name = 'my_simple_survey/Joke1184.html'


class Joke1185(JokePage):
    template_name = 'my_simple_survey/Joke1185.html'


class Joke1186(JokePage):
    template_name = 'my_simple_survey/Joke1186.html'


class Joke1187(JokePage):
    template_name = 'my_simple_survey/Joke1187.html'


class Joke1188(JokePage):
    template_name = 'my_simple_survey/Joke1188.html'


class Joke1189(JokePage):
    template_name = 'my_simple_survey/Joke1189.html'


class Joke1190(JokePage):
    template_name = 'my_simple_survey/Joke1190.html'


class Joke1191(JokePage):
    template_name = 'my_simple_survey/Joke1191.html'


class Joke1192(JokePage):
    template_name = 'my_simple_survey/Joke1192.html'


class Joke1193(JokePage):
    template_name = 'my_simple_survey/Joke1193.html'


class Joke1194(JokePage):
    template_name = 'my_simple_survey/Joke1194.html'


class Joke1195(JokePage):
    template_name = 'my_simple_survey/Joke1195.html'


class Joke1196(JokePage):
    template_name = 'my_simple_survey/Joke1196.html'


class Joke1197(JokePage):
    template_name = 'my_simple_survey/Joke1197.html'


class Joke1198(JokePage):
    template_name = 'my_simple_survey/Joke1198.html'


class Joke1199(JokePage):
    template_name = 'my_simple_survey/Joke1199.html'


class Joke1200(JokePage):
    template_name = 'my_simple_survey/Joke1200.html'


class Joke1201(JokePage):
    template_name = 'my_simple_survey/Joke1201.html'


class Joke1202(JokePage):
    template_name = 'my_simple_survey/Joke1202.html'


class Joke1203(JokePage):
    template_name = 'my_simple_survey/Joke1203.html'


class Joke1204(JokePage):
    template_name = 'my_simple_survey/Joke1204.html'


class Joke1205(JokePage):
    template_name = 'my_simple_survey/Joke1205.html'


class Joke1206(JokePage):
    template_name = 'my_simple_survey/Joke1206.html'


class Joke1207(JokePage):
    template_name = 'my_simple_survey/Joke1207.html'


class Joke1208(JokePage):
    template_name = 'my_simple_survey/Joke1208.html'


class Joke1209(JokePage):
    template_name = 'my_simple_survey/Joke1209.html'


class Joke1210(JokePage):
    template_name = 'my_simple_survey/Joke1210.html'


class Joke1211(JokePage):
    template_name = 'my_simple_survey/Joke1211.html'


class Joke1212(JokePage):
    template_name = 'my_simple_survey/Joke1212.html'


class Joke1213(JokePage):
    template_name = 'my_simple_survey/Joke1213.html'


class Joke1214(JokePage):
    template_name = 'my_simple_survey/Joke1214.html'


class Joke1215(JokePage):
    template_name = 'my_simple_survey/Joke1215.html'


class Joke1216(JokePage):
    template_name = 'my_simple_survey/Joke1216.html'


class Joke1217(JokePage):
    template_name = 'my_simple_survey/Joke1217.html'


class Joke1218(JokePage):
    template_name = 'my_simple_survey/Joke1218.html'


class Joke1219(JokePage):
    template_name = 'my_simple_survey/Joke1219.html'


class Joke1220(JokePage):
    template_name = 'my_simple_survey/Joke1220.html'


class Joke1221(JokePage):
    template_name = 'my_simple_survey/Joke1221.html'


class Joke1222(JokePage):
    template_name = 'my_simple_survey/Joke1222.html'


class Joke1223(JokePage):
    template_name = 'my_simple_survey/Joke1223.html'


class Joke1224(JokePage):
    template_name = 'my_simple_survey/Joke1224.html'


class Joke1225(JokePage):
    template_name = 'my_simple_survey/Joke1225.html'


class Joke1226(JokePage):
    template_name = 'my_simple_survey/Joke1226.html'


class Joke1227(JokePage):
    template_name = 'my_simple_survey/Joke1227.html'


class Joke1228(JokePage):
    template_name = 'my_simple_survey/Joke1228.html'


class Joke1229(JokePage):
    template_name = 'my_simple_survey/Joke1229.html'


class Joke1230(JokePage):
    template_name = 'my_simple_survey/Joke1230.html'


class Joke1231(JokePage):
    template_name = 'my_simple_survey/Joke1231.html'


class Joke1232(JokePage):
    template_name = 'my_simple_survey/Joke1232.html'


class Joke1233(JokePage):
    template_name = 'my_simple_survey/Joke1233.html'


class Joke1234(JokePage):
    template_name = 'my_simple_survey/Joke1234.html'


class Joke1235(JokePage):
    template_name = 'my_simple_survey/Joke1235.html'


class Joke1236(JokePage):
    template_name = 'my_simple_survey/Joke1236.html'


class Joke1237(JokePage):
    template_name = 'my_simple_survey/Joke1237.html'


class Joke1238(JokePage):
    template_name = 'my_simple_survey/Joke1238.html'


class Joke1239(JokePage):
    template_name = 'my_simple_survey/Joke1239.html'


class Joke1240(JokePage):
    template_name = 'my_simple_survey/Joke1240.html'


class Joke1241(JokePage):
    template_name = 'my_simple_survey/Joke1241.html'


class Joke1242(JokePage):
    template_name = 'my_simple_survey/Joke1242.html'


class Joke1243(JokePage):
    template_name = 'my_simple_survey/Joke1243.html'


class Joke1244(JokePage):
    template_name = 'my_simple_survey/Joke1244.html'


class Joke1245(JokePage):
    template_name = 'my_simple_survey/Joke1245.html'


class Joke1246(JokePage):
    template_name = 'my_simple_survey/Joke1246.html'


class Joke1247(JokePage):
    template_name = 'my_simple_survey/Joke1247.html'


class Joke1248(JokePage):
    template_name = 'my_simple_survey/Joke1248.html'


class Joke1249(JokePage):
    template_name = 'my_simple_survey/Joke1249.html'


class Joke1250(JokePage):
    template_name = 'my_simple_survey/Joke1250.html'


class Joke1251(JokePage):
    template_name = 'my_simple_survey/Joke1251.html'


class Joke1252(JokePage):
    template_name = 'my_simple_survey/Joke1252.html'


class Joke1253(JokePage):
    template_name = 'my_simple_survey/Joke1253.html'


class Joke1254(JokePage):
    template_name = 'my_simple_survey/Joke1254.html'


class Joke1255(JokePage):
    template_name = 'my_simple_survey/Joke1255.html'


class Joke1256(JokePage):
    template_name = 'my_simple_survey/Joke1256.html'


class Joke1257(JokePage):
    template_name = 'my_simple_survey/Joke1257.html'


class Joke1258(JokePage):
    template_name = 'my_simple_survey/Joke1258.html'


class Joke1259(JokePage):
    template_name = 'my_simple_survey/Joke1259.html'


class Joke1260(JokePage):
    template_name = 'my_simple_survey/Joke1260.html'


class Joke1261(JokePage):
    template_name = 'my_simple_survey/Joke1261.html'


class Joke1262(JokePage):
    template_name = 'my_simple_survey/Joke1262.html'


class Joke1263(JokePage):
    template_name = 'my_simple_survey/Joke1263.html'


class Joke1264(JokePage):
    template_name = 'my_simple_survey/Joke1264.html'


class Joke1265(JokePage):
    template_name = 'my_simple_survey/Joke1265.html'


class Joke1266(JokePage):
    template_name = 'my_simple_survey/Joke1266.html'


class Joke1267(JokePage):
    template_name = 'my_simple_survey/Joke1267.html'


class Joke1268(JokePage):
    template_name = 'my_simple_survey/Joke1268.html'


class Joke1269(JokePage):
    template_name = 'my_simple_survey/Joke1269.html'


class Joke1270(JokePage):
    template_name = 'my_simple_survey/Joke1270.html'


class Joke1271(JokePage):
    template_name = 'my_simple_survey/Joke1271.html'


class Joke1272(JokePage):
    template_name = 'my_simple_survey/Joke1272.html'


class Joke1273(JokePage):
    template_name = 'my_simple_survey/Joke1273.html'


class Joke1274(JokePage):
    template_name = 'my_simple_survey/Joke1274.html'


class Joke1275(JokePage):
    template_name = 'my_simple_survey/Joke1275.html'


class Joke1276(JokePage):
    template_name = 'my_simple_survey/Joke1276.html'


class Joke1277(JokePage):
    template_name = 'my_simple_survey/Joke1277.html'


class Joke1278(JokePage):
    template_name = 'my_simple_survey/Joke1278.html'


class Joke1279(JokePage):
    template_name = 'my_simple_survey/Joke1279.html'


class Joke1280(JokePage):
    template_name = 'my_simple_survey/Joke1280.html'


class Joke1281(JokePage):
    template_name = 'my_simple_survey/Joke1281.html'


class Joke1282(JokePage):
    template_name = 'my_simple_survey/Joke1282.html'


class Joke1283(JokePage):
    template_name = 'my_simple_survey/Joke1283.html'


class Joke1284(JokePage):
    template_name = 'my_simple_survey/Joke1284.html'


class Joke1285(JokePage):
    template_name = 'my_simple_survey/Joke1285.html'


class Joke1286(JokePage):
    template_name = 'my_simple_survey/Joke1286.html'


class Joke1287(JokePage):
    template_name = 'my_simple_survey/Joke1287.html'


class Joke1288(JokePage):
    template_name = 'my_simple_survey/Joke1288.html'


class Joke1289(JokePage):
    template_name = 'my_simple_survey/Joke1289.html'


class Joke1290(JokePage):
    template_name = 'my_simple_survey/Joke1290.html'


class Joke1291(JokePage):
    template_name = 'my_simple_survey/Joke1291.html'


class Joke1292(JokePage):
    template_name = 'my_simple_survey/Joke1292.html'


class Joke1293(JokePage):
    template_name = 'my_simple_survey/Joke1293.html'


class Joke1294(JokePage):
    template_name = 'my_simple_survey/Joke1294.html'


class Joke1295(JokePage):
    template_name = 'my_simple_survey/Joke1295.html'


class Joke1296(JokePage):
    template_name = 'my_simple_survey/Joke1296.html'


class Joke1297(JokePage):
    template_name = 'my_simple_survey/Joke1297.html'


class Joke1298(JokePage):
    template_name = 'my_simple_survey/Joke1298.html'


class Joke1299(JokePage):
    template_name = 'my_simple_survey/Joke1299.html'


class Joke1300(JokePage):
    template_name = 'my_simple_survey/Joke1300.html'


class Joke1301(JokePage):
    template_name = 'my_simple_survey/Joke1301.html'


class Joke1302(JokePage):
    template_name = 'my_simple_survey/Joke1302.html'


class Joke1303(JokePage):
    template_name = 'my_simple_survey/Joke1303.html'


class Joke1304(JokePage):
    template_name = 'my_simple_survey/Joke1304.html'


class Joke1305(JokePage):
    template_name = 'my_simple_survey/Joke1305.html'


class Joke1306(JokePage):
    template_name = 'my_simple_survey/Joke1306.html'


class Joke1307(JokePage):
    template_name = 'my_simple_survey/Joke1307.html'


class Joke1308(JokePage):
    template_name = 'my_simple_survey/Joke1308.html'


class Joke1309(JokePage):
    template_name = 'my_simple_survey/Joke1309.html'


class Joke1310(JokePage):
    template_name = 'my_simple_survey/Joke1310.html'


class Joke1311(JokePage):
    template_name = 'my_simple_survey/Joke1311.html'


class Joke1312(JokePage):
    template_name = 'my_simple_survey/Joke1312.html'


class Joke1313(JokePage):
    template_name = 'my_simple_survey/Joke1313.html'


class Joke1314(JokePage):
    template_name = 'my_simple_survey/Joke1314.html'


class Joke1315(JokePage):
    template_name = 'my_simple_survey/Joke1315.html'


class Joke1316(JokePage):
    template_name = 'my_simple_survey/Joke1316.html'


class Joke1317(JokePage):
    template_name = 'my_simple_survey/Joke1317.html'


class Joke1318(JokePage):
    template_name = 'my_simple_survey/Joke1318.html'


class Joke1319(JokePage):
    template_name = 'my_simple_survey/Joke1319.html'


class Joke1320(JokePage):
    template_name = 'my_simple_survey/Joke1320.html'


class Joke1321(JokePage):
    template_name = 'my_simple_survey/Joke1321.html'


class Joke1322(JokePage):
    template_name = 'my_simple_survey/Joke1322.html'


class Joke1323(JokePage):
    template_name = 'my_simple_survey/Joke1323.html'


class Joke1324(JokePage):
    template_name = 'my_simple_survey/Joke1324.html'


class Joke1325(JokePage):
    template_name = 'my_simple_survey/Joke1325.html'


class Joke1326(JokePage):
    template_name = 'my_simple_survey/Joke1326.html'


class Joke1327(JokePage):
    template_name = 'my_simple_survey/Joke1327.html'


class Joke1328(JokePage):
    template_name = 'my_simple_survey/Joke1328.html'


class Joke1329(JokePage):
    template_name = 'my_simple_survey/Joke1329.html'


class Joke1330(JokePage):
    template_name = 'my_simple_survey/Joke1330.html'


class Joke1331(JokePage):
    template_name = 'my_simple_survey/Joke1331.html'


class Joke1332(JokePage):
    template_name = 'my_simple_survey/Joke1332.html'


class Joke1333(JokePage):
    template_name = 'my_simple_survey/Joke1333.html'


class Joke1334(JokePage):
    template_name = 'my_simple_survey/Joke1334.html'


class Joke1335(JokePage):
    template_name = 'my_simple_survey/Joke1335.html'


class Joke1336(JokePage):
    template_name = 'my_simple_survey/Joke1336.html'


class Joke1337(JokePage):
    template_name = 'my_simple_survey/Joke1337.html'


class Joke1338(JokePage):
    template_name = 'my_simple_survey/Joke1338.html'


class Joke1339(JokePage):
    template_name = 'my_simple_survey/Joke1339.html'


class Joke1340(JokePage):
    template_name = 'my_simple_survey/Joke1340.html'


class Joke1341(JokePage):
    template_name = 'my_simple_survey/Joke1341.html'


class Joke1342(JokePage):
    template_name = 'my_simple_survey/Joke1342.html'


class Joke1343(JokePage):
    template_name = 'my_simple_survey/Joke1343.html'


class Joke1344(JokePage):
    template_name = 'my_simple_survey/Joke1344.html'


class Joke1345(JokePage):
    template_name = 'my_simple_survey/Joke1345.html'


class Joke1346(JokePage):
    template_name = 'my_simple_survey/Joke1346.html'


class Joke1347(JokePage):
    template_name = 'my_simple_survey/Joke1347.html'


class Joke1348(JokePage):
    template_name = 'my_simple_survey/Joke1348.html'


class Joke1349(JokePage):
    template_name = 'my_simple_survey/Joke1349.html'


class Joke1350(JokePage):
    template_name = 'my_simple_survey/Joke1350.html'


class Joke1351(JokePage):
    template_name = 'my_simple_survey/Joke1351.html'


class Joke1352(JokePage):
    template_name = 'my_simple_survey/Joke1352.html'


class Joke1353(JokePage):
    template_name = 'my_simple_survey/Joke1353.html'


class Joke1354(JokePage):
    template_name = 'my_simple_survey/Joke1354.html'


class Joke1355(JokePage):
    template_name = 'my_simple_survey/Joke1355.html'


class Joke1356(JokePage):
    template_name = 'my_simple_survey/Joke1356.html'


class Joke1357(JokePage):
    template_name = 'my_simple_survey/Joke1357.html'


class Joke1358(JokePage):
    template_name = 'my_simple_survey/Joke1358.html'


class Joke1359(JokePage):
    template_name = 'my_simple_survey/Joke1359.html'


class Joke1360(JokePage):
    template_name = 'my_simple_survey/Joke1360.html'


class Joke1361(JokePage):
    template_name = 'my_simple_survey/Joke1361.html'


class Joke1362(JokePage):
    template_name = 'my_simple_survey/Joke1362.html'


class Joke1363(JokePage):
    template_name = 'my_simple_survey/Joke1363.html'


class Joke1364(JokePage):
    template_name = 'my_simple_survey/Joke1364.html'


class Joke1365(JokePage):
    template_name = 'my_simple_survey/Joke1365.html'


class Joke1366(JokePage):
    template_name = 'my_simple_survey/Joke1366.html'


class Joke1367(JokePage):
    template_name = 'my_simple_survey/Joke1367.html'


class Joke1368(JokePage):
    template_name = 'my_simple_survey/Joke1368.html'


class Joke1369(JokePage):
    template_name = 'my_simple_survey/Joke1369.html'


class Joke1370(JokePage):
    template_name = 'my_simple_survey/Joke1370.html'


class Joke1371(JokePage):
    template_name = 'my_simple_survey/Joke1371.html'


class Joke1372(JokePage):
    template_name = 'my_simple_survey/Joke1372.html'


class Joke1373(JokePage):
    template_name = 'my_simple_survey/Joke1373.html'


class Joke1374(JokePage):
    template_name = 'my_simple_survey/Joke1374.html'


class Joke1375(JokePage):
    template_name = 'my_simple_survey/Joke1375.html'


class Joke1376(JokePage):
    template_name = 'my_simple_survey/Joke1376.html'


class Joke1377(JokePage):
    template_name = 'my_simple_survey/Joke1377.html'


class Joke1378(JokePage):
    template_name = 'my_simple_survey/Joke1378.html'


class Joke1379(JokePage):
    template_name = 'my_simple_survey/Joke1379.html'


class Joke1380(JokePage):
    template_name = 'my_simple_survey/Joke1380.html'


class Joke1381(JokePage):
    template_name = 'my_simple_survey/Joke1381.html'


class Joke1382(JokePage):
    template_name = 'my_simple_survey/Joke1382.html'


class Joke1383(JokePage):
    template_name = 'my_simple_survey/Joke1383.html'


class Joke1384(JokePage):
    template_name = 'my_simple_survey/Joke1384.html'


class Joke1385(JokePage):
    template_name = 'my_simple_survey/Joke1385.html'


class Joke1386(JokePage):
    template_name = 'my_simple_survey/Joke1386.html'


class Joke1387(JokePage):
    template_name = 'my_simple_survey/Joke1387.html'


class Joke1388(JokePage):
    template_name = 'my_simple_survey/Joke1388.html'


class Joke1389(JokePage):
    template_name = 'my_simple_survey/Joke1389.html'


class Joke1390(JokePage):
    template_name = 'my_simple_survey/Joke1390.html'


class Joke1391(JokePage):
    template_name = 'my_simple_survey/Joke1391.html'


class Joke1392(JokePage):
    template_name = 'my_simple_survey/Joke1392.html'


class Joke1393(JokePage):
    template_name = 'my_simple_survey/Joke1393.html'


class Joke1394(JokePage):
    template_name = 'my_simple_survey/Joke1394.html'


class Joke1395(JokePage):
    template_name = 'my_simple_survey/Joke1395.html'


class Joke1396(JokePage):
    template_name = 'my_simple_survey/Joke1396.html'


class Joke1397(JokePage):
    template_name = 'my_simple_survey/Joke1397.html'


class Joke1398(JokePage):
    template_name = 'my_simple_survey/Joke1398.html'


class Joke1399(JokePage):
    template_name = 'my_simple_survey/Joke1399.html'


class Joke1400(JokePage):
    template_name = 'my_simple_survey/Joke1400.html'


class Joke1401(JokePage):
    template_name = 'my_simple_survey/Joke1401.html'


class Joke1402(JokePage):
    template_name = 'my_simple_survey/Joke1402.html'


class Joke1403(JokePage):
    template_name = 'my_simple_survey/Joke1403.html'


class Joke1404(JokePage):
    template_name = 'my_simple_survey/Joke1404.html'


class Joke1405(JokePage):
    template_name = 'my_simple_survey/Joke1405.html'


class Joke1406(JokePage):
    template_name = 'my_simple_survey/Joke1406.html'


class Joke1407(JokePage):
    template_name = 'my_simple_survey/Joke1407.html'


class Joke1408(JokePage):
    template_name = 'my_simple_survey/Joke1408.html'


class Joke1409(JokePage):
    template_name = 'my_simple_survey/Joke1409.html'


class Joke1410(JokePage):
    template_name = 'my_simple_survey/Joke1410.html'


class Joke1411(JokePage):
    template_name = 'my_simple_survey/Joke1411.html'


class Joke1412(JokePage):
    template_name = 'my_simple_survey/Joke1412.html'


class Joke1413(JokePage):
    template_name = 'my_simple_survey/Joke1413.html'


class Joke1414(JokePage):
    template_name = 'my_simple_survey/Joke1414.html'


class Joke1415(JokePage):
    template_name = 'my_simple_survey/Joke1415.html'


class Joke1416(JokePage):
    template_name = 'my_simple_survey/Joke1416.html'


class Joke1417(JokePage):
    template_name = 'my_simple_survey/Joke1417.html'


class Joke1418(JokePage):
    template_name = 'my_simple_survey/Joke1418.html'


class Joke1419(JokePage):
    template_name = 'my_simple_survey/Joke1419.html'


class Joke1420(JokePage):
    template_name = 'my_simple_survey/Joke1420.html'


class Joke1421(JokePage):
    template_name = 'my_simple_survey/Joke1421.html'


class Joke1422(JokePage):
    template_name = 'my_simple_survey/Joke1422.html'


class Joke1423(JokePage):
    template_name = 'my_simple_survey/Joke1423.html'


class Joke1424(JokePage):
    template_name = 'my_simple_survey/Joke1424.html'


class Joke1425(JokePage):
    template_name = 'my_simple_survey/Joke1425.html'


class Joke1426(JokePage):
    template_name = 'my_simple_survey/Joke1426.html'


class Joke1427(JokePage):
    template_name = 'my_simple_survey/Joke1427.html'


class Joke1428(JokePage):
    template_name = 'my_simple_survey/Joke1428.html'


class Joke1429(JokePage):
    template_name = 'my_simple_survey/Joke1429.html'


class Joke1430(JokePage):
    template_name = 'my_simple_survey/Joke1430.html'


class Joke1431(JokePage):
    template_name = 'my_simple_survey/Joke1431.html'


class Joke1432(JokePage):
    template_name = 'my_simple_survey/Joke1432.html'


class Joke1433(JokePage):
    template_name = 'my_simple_survey/Joke1433.html'


class Joke1434(JokePage):
    template_name = 'my_simple_survey/Joke1434.html'


class Joke1435(JokePage):
    template_name = 'my_simple_survey/Joke1435.html'


class Joke1436(JokePage):
    template_name = 'my_simple_survey/Joke1436.html'


class Joke1437(JokePage):
    template_name = 'my_simple_survey/Joke1437.html'


class Joke1438(JokePage):
    template_name = 'my_simple_survey/Joke1438.html'


class Joke1439(JokePage):
    template_name = 'my_simple_survey/Joke1439.html'


class Joke1440(JokePage):
    template_name = 'my_simple_survey/Joke1440.html'


class Joke1441(JokePage):
    template_name = 'my_simple_survey/Joke1441.html'


class Joke1442(JokePage):
    template_name = 'my_simple_survey/Joke1442.html'


class Joke1443(JokePage):
    template_name = 'my_simple_survey/Joke1443.html'


class Joke1444(JokePage):
    template_name = 'my_simple_survey/Joke1444.html'


class Joke1445(JokePage):
    template_name = 'my_simple_survey/Joke1445.html'


class Joke1446(JokePage):
    template_name = 'my_simple_survey/Joke1446.html'


class Joke1447(JokePage):
    template_name = 'my_simple_survey/Joke1447.html'


class Joke1448(JokePage):
    template_name = 'my_simple_survey/Joke1448.html'


class Joke1449(JokePage):
    template_name = 'my_simple_survey/Joke1449.html'


class Joke1450(JokePage):
    template_name = 'my_simple_survey/Joke1450.html'


class Joke1451(JokePage):
    template_name = 'my_simple_survey/Joke1451.html'


class Joke1452(JokePage):
    template_name = 'my_simple_survey/Joke1452.html'


class Joke1453(JokePage):
    template_name = 'my_simple_survey/Joke1453.html'


class Joke1454(JokePage):
    template_name = 'my_simple_survey/Joke1454.html'


class Joke1455(JokePage):
    template_name = 'my_simple_survey/Joke1455.html'


class Joke1456(JokePage):
    template_name = 'my_simple_survey/Joke1456.html'


class Joke1457(JokePage):
    template_name = 'my_simple_survey/Joke1457.html'


class Joke1458(JokePage):
    template_name = 'my_simple_survey/Joke1458.html'


class Joke1459(JokePage):
    template_name = 'my_simple_survey/Joke1459.html'


class Joke1460(JokePage):
    template_name = 'my_simple_survey/Joke1460.html'


class Joke1461(JokePage):
    template_name = 'my_simple_survey/Joke1461.html'


class Joke1462(JokePage):
    template_name = 'my_simple_survey/Joke1462.html'


class Joke1463(JokePage):
    template_name = 'my_simple_survey/Joke1463.html'


class Joke1464(JokePage):
    template_name = 'my_simple_survey/Joke1464.html'


class Joke1465(JokePage):
    template_name = 'my_simple_survey/Joke1465.html'


class Joke1466(JokePage):
    template_name = 'my_simple_survey/Joke1466.html'


class Joke1467(JokePage):
    template_name = 'my_simple_survey/Joke1467.html'


class Joke1468(JokePage):
    template_name = 'my_simple_survey/Joke1468.html'


class Joke1469(JokePage):
    template_name = 'my_simple_survey/Joke1469.html'


class Joke1470(JokePage):
    template_name = 'my_simple_survey/Joke1470.html'


class Joke1471(JokePage):
    template_name = 'my_simple_survey/Joke1471.html'


class Joke1472(JokePage):
    template_name = 'my_simple_survey/Joke1472.html'


class Joke1473(JokePage):
    template_name = 'my_simple_survey/Joke1473.html'


class Joke1474(JokePage):
    template_name = 'my_simple_survey/Joke1474.html'


class Joke1475(JokePage):
    template_name = 'my_simple_survey/Joke1475.html'


class Joke1476(JokePage):
    template_name = 'my_simple_survey/Joke1476.html'


class Joke1477(JokePage):
    template_name = 'my_simple_survey/Joke1477.html'


class Joke1478(JokePage):
    template_name = 'my_simple_survey/Joke1478.html'


class Joke1479(JokePage):
    template_name = 'my_simple_survey/Joke1479.html'


class Joke1480(JokePage):
    template_name = 'my_simple_survey/Joke1480.html'


class Joke1481(JokePage):
    template_name = 'my_simple_survey/Joke1481.html'


class Joke1482(JokePage):
    template_name = 'my_simple_survey/Joke1482.html'


class Joke1483(JokePage):
    template_name = 'my_simple_survey/Joke1483.html'


class Joke1484(JokePage):
    template_name = 'my_simple_survey/Joke1484.html'


class Joke1485(JokePage):
    template_name = 'my_simple_survey/Joke1485.html'


class Joke1486(JokePage):
    template_name = 'my_simple_survey/Joke1486.html'


class Joke1487(JokePage):
    template_name = 'my_simple_survey/Joke1487.html'


class Joke1488(JokePage):
    template_name = 'my_simple_survey/Joke1488.html'


class Joke1489(JokePage):
    template_name = 'my_simple_survey/Joke1489.html'


class Joke1490(JokePage):
    template_name = 'my_simple_survey/Joke1490.html'


class Joke1491(JokePage):
    template_name = 'my_simple_survey/Joke1491.html'


class Joke1492(JokePage):
    template_name = 'my_simple_survey/Joke1492.html'


class Joke1493(JokePage):
    template_name = 'my_simple_survey/Joke1493.html'


class Joke1494(JokePage):
    template_name = 'my_simple_survey/Joke1494.html'


class Joke1495(JokePage):
    template_name = 'my_simple_survey/Joke1495.html'


class Joke1496(JokePage):
    template_name = 'my_simple_survey/Joke1496.html'


class Joke1497(JokePage):
    template_name = 'my_simple_survey/Joke1497.html'


class Joke1498(JokePage):
    template_name = 'my_simple_survey/Joke1498.html'


class Joke1499(JokePage):
    template_name = 'my_simple_survey/Joke1499.html'


class Joke1500(JokePage):
    template_name = 'my_simple_survey/Joke1500.html'


class Joke1501(JokePage):
    template_name = 'my_simple_survey/Joke1501.html'


class Joke1502(JokePage):
    template_name = 'my_simple_survey/Joke1502.html'


class Joke1503(JokePage):
    template_name = 'my_simple_survey/Joke1503.html'


class Joke1504(JokePage):
    template_name = 'my_simple_survey/Joke1504.html'


class Joke1505(JokePage):
    template_name = 'my_simple_survey/Joke1505.html'


class Joke1506(JokePage):
    template_name = 'my_simple_survey/Joke1506.html'


class Joke1507(JokePage):
    template_name = 'my_simple_survey/Joke1507.html'


class Joke1508(JokePage):
    template_name = 'my_simple_survey/Joke1508.html'


class Joke1509(JokePage):
    template_name = 'my_simple_survey/Joke1509.html'


class Joke1510(JokePage):
    template_name = 'my_simple_survey/Joke1510.html'


class Joke1511(JokePage):
    template_name = 'my_simple_survey/Joke1511.html'


class Joke1512(JokePage):
    template_name = 'my_simple_survey/Joke1512.html'


class Joke1513(JokePage):
    template_name = 'my_simple_survey/Joke1513.html'


class Joke1514(JokePage):
    template_name = 'my_simple_survey/Joke1514.html'


class Joke1515(JokePage):
    template_name = 'my_simple_survey/Joke1515.html'


class Joke1516(JokePage):
    template_name = 'my_simple_survey/Joke1516.html'


class Joke1517(JokePage):
    template_name = 'my_simple_survey/Joke1517.html'


class Joke1518(JokePage):
    template_name = 'my_simple_survey/Joke1518.html'


class Joke1519(JokePage):
    template_name = 'my_simple_survey/Joke1519.html'


class Joke1520(JokePage):
    template_name = 'my_simple_survey/Joke1520.html'


class Joke1521(JokePage):
    template_name = 'my_simple_survey/Joke1521.html'


class Joke1522(JokePage):
    template_name = 'my_simple_survey/Joke1522.html'


class Joke1523(JokePage):
    template_name = 'my_simple_survey/Joke1523.html'


class Joke1524(JokePage):
    template_name = 'my_simple_survey/Joke1524.html'


class Joke1525(JokePage):
    template_name = 'my_simple_survey/Joke1525.html'


class Joke1526(JokePage):
    template_name = 'my_simple_survey/Joke1526.html'


class Joke1527(JokePage):
    template_name = 'my_simple_survey/Joke1527.html'


class Joke1528(JokePage):
    template_name = 'my_simple_survey/Joke1528.html'


class Joke1529(JokePage):
    template_name = 'my_simple_survey/Joke1529.html'


class Joke1530(JokePage):
    template_name = 'my_simple_survey/Joke1530.html'


class Joke1531(JokePage):
    template_name = 'my_simple_survey/Joke1531.html'


class Joke1532(JokePage):
    template_name = 'my_simple_survey/Joke1532.html'


class Joke1533(JokePage):
    template_name = 'my_simple_survey/Joke1533.html'


class Joke1534(JokePage):
    template_name = 'my_simple_survey/Joke1534.html'


class Joke1535(JokePage):
    template_name = 'my_simple_survey/Joke1535.html'


class Joke1536(JokePage):
    template_name = 'my_simple_survey/Joke1536.html'


class Joke1537(JokePage):
    template_name = 'my_simple_survey/Joke1537.html'


class Joke1538(JokePage):
    template_name = 'my_simple_survey/Joke1538.html'


class Joke1539(JokePage):
    template_name = 'my_simple_survey/Joke1539.html'


class Joke1540(JokePage):
    template_name = 'my_simple_survey/Joke1540.html'


class Joke1541(JokePage):
    template_name = 'my_simple_survey/Joke1541.html'


class Joke1542(JokePage):
    template_name = 'my_simple_survey/Joke1542.html'


class Joke1543(JokePage):
    template_name = 'my_simple_survey/Joke1543.html'


class Joke1544(JokePage):
    template_name = 'my_simple_survey/Joke1544.html'


class Joke1545(JokePage):
    template_name = 'my_simple_survey/Joke1545.html'


class Joke1546(JokePage):
    template_name = 'my_simple_survey/Joke1546.html'


class Joke1547(JokePage):
    template_name = 'my_simple_survey/Joke1547.html'


class Joke1548(JokePage):
    template_name = 'my_simple_survey/Joke1548.html'


class Joke1549(JokePage):
    template_name = 'my_simple_survey/Joke1549.html'


class Joke1550(JokePage):
    template_name = 'my_simple_survey/Joke1550.html'


class Joke1551(JokePage):
    template_name = 'my_simple_survey/Joke1551.html'


class Joke1552(JokePage):
    template_name = 'my_simple_survey/Joke1552.html'


class Joke1553(JokePage):
    template_name = 'my_simple_survey/Joke1553.html'


class Joke1554(JokePage):
    template_name = 'my_simple_survey/Joke1554.html'


class Joke1555(JokePage):
    template_name = 'my_simple_survey/Joke1555.html'


class Joke1556(JokePage):
    template_name = 'my_simple_survey/Joke1556.html'


class Joke1557(JokePage):
    template_name = 'my_simple_survey/Joke1557.html'


class Joke1558(JokePage):
    template_name = 'my_simple_survey/Joke1558.html'


class Joke1559(JokePage):
    template_name = 'my_simple_survey/Joke1559.html'


class Joke1560(JokePage):
    template_name = 'my_simple_survey/Joke1560.html'


class Joke1561(JokePage):
    template_name = 'my_simple_survey/Joke1561.html'


class Joke1562(JokePage):
    template_name = 'my_simple_survey/Joke1562.html'


class Joke1563(JokePage):
    template_name = 'my_simple_survey/Joke1563.html'


class Joke1564(JokePage):
    template_name = 'my_simple_survey/Joke1564.html'


class Joke1565(JokePage):
    template_name = 'my_simple_survey/Joke1565.html'


class Joke1566(JokePage):
    template_name = 'my_simple_survey/Joke1566.html'


class Joke1567(JokePage):
    template_name = 'my_simple_survey/Joke1567.html'


class Joke1568(JokePage):
    template_name = 'my_simple_survey/Joke1568.html'


class Joke1569(JokePage):
    template_name = 'my_simple_survey/Joke1569.html'


class Joke1570(JokePage):
    template_name = 'my_simple_survey/Joke1570.html'


class Joke1571(JokePage):
    template_name = 'my_simple_survey/Joke1571.html'


class Joke1572(JokePage):
    template_name = 'my_simple_survey/Joke1572.html'


class Joke1573(JokePage):
    template_name = 'my_simple_survey/Joke1573.html'


class Joke1574(JokePage):
    template_name = 'my_simple_survey/Joke1574.html'


class Joke1575(JokePage):
    template_name = 'my_simple_survey/Joke1575.html'


class Joke1576(JokePage):
    template_name = 'my_simple_survey/Joke1576.html'


class Joke1577(JokePage):
    template_name = 'my_simple_survey/Joke1577.html'


class Joke1578(JokePage):
    template_name = 'my_simple_survey/Joke1578.html'


class Joke1579(JokePage):
    template_name = 'my_simple_survey/Joke1579.html'


class Joke1580(JokePage):
    template_name = 'my_simple_survey/Joke1580.html'


class Joke1581(JokePage):
    template_name = 'my_simple_survey/Joke1581.html'


class Joke1582(JokePage):
    template_name = 'my_simple_survey/Joke1582.html'


class Joke1583(JokePage):
    template_name = 'my_simple_survey/Joke1583.html'


class Joke1584(JokePage):
    template_name = 'my_simple_survey/Joke1584.html'


class Joke1585(JokePage):
    template_name = 'my_simple_survey/Joke1585.html'


class Joke1586(JokePage):
    template_name = 'my_simple_survey/Joke1586.html'


class Joke1587(JokePage):
    template_name = 'my_simple_survey/Joke1587.html'


class Joke1588(JokePage):
    template_name = 'my_simple_survey/Joke1588.html'


class Joke1589(JokePage):
    template_name = 'my_simple_survey/Joke1589.html'


class Joke1590(JokePage):
    template_name = 'my_simple_survey/Joke1590.html'


class Joke1591(JokePage):
    template_name = 'my_simple_survey/Joke1591.html'


class Joke1592(JokePage):
    template_name = 'my_simple_survey/Joke1592.html'


class Joke1593(JokePage):
    template_name = 'my_simple_survey/Joke1593.html'


class Joke1594(JokePage):
    template_name = 'my_simple_survey/Joke1594.html'


class Joke1595(JokePage):
    template_name = 'my_simple_survey/Joke1595.html'


class Joke1596(JokePage):
    template_name = 'my_simple_survey/Joke1596.html'


class Joke1597(JokePage):
    template_name = 'my_simple_survey/Joke1597.html'


class Joke1598(JokePage):
    template_name = 'my_simple_survey/Joke1598.html'


class Joke1599(JokePage):
    template_name = 'my_simple_survey/Joke1599.html'


class Joke1600(JokePage):
    template_name = 'my_simple_survey/Joke1600.html'


class Joke1601(JokePage):
    template_name = 'my_simple_survey/Joke1601.html'


class Joke1602(JokePage):
    template_name = 'my_simple_survey/Joke1602.html'


class Joke1603(JokePage):
    template_name = 'my_simple_survey/Joke1603.html'


class Joke1604(JokePage):
    template_name = 'my_simple_survey/Joke1604.html'


class Joke1605(JokePage):
    template_name = 'my_simple_survey/Joke1605.html'


class Joke1606(JokePage):
    template_name = 'my_simple_survey/Joke1606.html'


class Joke1607(JokePage):
    template_name = 'my_simple_survey/Joke1607.html'


class Joke1608(JokePage):
    template_name = 'my_simple_survey/Joke1608.html'


class Joke1609(JokePage):
    template_name = 'my_simple_survey/Joke1609.html'


class Joke1610(JokePage):
    template_name = 'my_simple_survey/Joke1610.html'


class Joke1611(JokePage):
    template_name = 'my_simple_survey/Joke1611.html'


class Joke1612(JokePage):
    template_name = 'my_simple_survey/Joke1612.html'


class Joke1613(JokePage):
    template_name = 'my_simple_survey/Joke1613.html'


class Joke1614(JokePage):
    template_name = 'my_simple_survey/Joke1614.html'


class Joke1615(JokePage):
    template_name = 'my_simple_survey/Joke1615.html'


class Joke1616(JokePage):
    template_name = 'my_simple_survey/Joke1616.html'


class Joke1617(JokePage):
    template_name = 'my_simple_survey/Joke1617.html'


class Joke1618(JokePage):
    template_name = 'my_simple_survey/Joke1618.html'


class Joke1619(JokePage):
    template_name = 'my_simple_survey/Joke1619.html'


class Joke1620(JokePage):
    template_name = 'my_simple_survey/Joke1620.html'


class Joke1621(JokePage):
    template_name = 'my_simple_survey/Joke1621.html'


class Joke1622(JokePage):
    template_name = 'my_simple_survey/Joke1622.html'


class Joke1623(JokePage):
    template_name = 'my_simple_survey/Joke1623.html'


class Joke1624(JokePage):
    template_name = 'my_simple_survey/Joke1624.html'


class Joke1625(JokePage):
    template_name = 'my_simple_survey/Joke1625.html'


class Joke1626(JokePage):
    template_name = 'my_simple_survey/Joke1626.html'


class Joke1627(JokePage):
    template_name = 'my_simple_survey/Joke1627.html'


class Joke1628(JokePage):
    template_name = 'my_simple_survey/Joke1628.html'


class Joke1629(JokePage):
    template_name = 'my_simple_survey/Joke1629.html'


class Joke1630(JokePage):
    template_name = 'my_simple_survey/Joke1630.html'


class Joke1631(JokePage):
    template_name = 'my_simple_survey/Joke1631.html'


class Joke1632(JokePage):
    template_name = 'my_simple_survey/Joke1632.html'


class Joke1633(JokePage):
    template_name = 'my_simple_survey/Joke1633.html'


class Joke1634(JokePage):
    template_name = 'my_simple_survey/Joke1634.html'


class Joke1635(JokePage):
    template_name = 'my_simple_survey/Joke1635.html'


class Joke1636(JokePage):
    template_name = 'my_simple_survey/Joke1636.html'


class Joke1637(JokePage):
    template_name = 'my_simple_survey/Joke1637.html'


class Joke1638(JokePage):
    template_name = 'my_simple_survey/Joke1638.html'


class Joke1639(JokePage):
    template_name = 'my_simple_survey/Joke1639.html'


class Joke1640(JokePage):
    template_name = 'my_simple_survey/Joke1640.html'


class Joke1641(JokePage):
    template_name = 'my_simple_survey/Joke1641.html'


class Joke1642(JokePage):
    template_name = 'my_simple_survey/Joke1642.html'


class Joke1643(JokePage):
    template_name = 'my_simple_survey/Joke1643.html'


class Joke1644(JokePage):
    template_name = 'my_simple_survey/Joke1644.html'


class Joke1645(JokePage):
    template_name = 'my_simple_survey/Joke1645.html'


class Joke1646(JokePage):
    template_name = 'my_simple_survey/Joke1646.html'


class Joke1647(JokePage):
    template_name = 'my_simple_survey/Joke1647.html'


class Joke1648(JokePage):
    template_name = 'my_simple_survey/Joke1648.html'


class Joke1649(JokePage):
    template_name = 'my_simple_survey/Joke1649.html'


class Joke1650(JokePage):
    template_name = 'my_simple_survey/Joke1650.html'


class Joke1651(JokePage):
    template_name = 'my_simple_survey/Joke1651.html'


class Joke1652(JokePage):
    template_name = 'my_simple_survey/Joke1652.html'


class Joke1653(JokePage):
    template_name = 'my_simple_survey/Joke1653.html'


class Joke1654(JokePage):
    template_name = 'my_simple_survey/Joke1654.html'


class Joke1655(JokePage):
    template_name = 'my_simple_survey/Joke1655.html'


class Joke1656(JokePage):
    template_name = 'my_simple_survey/Joke1656.html'


class Joke1657(JokePage):
    template_name = 'my_simple_survey/Joke1657.html'


class Joke1658(JokePage):
    template_name = 'my_simple_survey/Joke1658.html'


class Joke1659(JokePage):
    template_name = 'my_simple_survey/Joke1659.html'


class Joke1660(JokePage):
    template_name = 'my_simple_survey/Joke1660.html'


class Joke1661(JokePage):
    template_name = 'my_simple_survey/Joke1661.html'


class Joke1662(JokePage):
    template_name = 'my_simple_survey/Joke1662.html'


class Joke1663(JokePage):
    template_name = 'my_simple_survey/Joke1663.html'


class Joke1664(JokePage):
    template_name = 'my_simple_survey/Joke1664.html'


class Joke1665(JokePage):
    template_name = 'my_simple_survey/Joke1665.html'


class Joke1666(JokePage):
    template_name = 'my_simple_survey/Joke1666.html'


class Joke1667(JokePage):
    template_name = 'my_simple_survey/Joke1667.html'


class Joke1668(JokePage):
    template_name = 'my_simple_survey/Joke1668.html'


class Joke1669(JokePage):
    template_name = 'my_simple_survey/Joke1669.html'


class Joke1670(JokePage):
    template_name = 'my_simple_survey/Joke1670.html'


class Joke1671(JokePage):
    template_name = 'my_simple_survey/Joke1671.html'


class Joke1672(JokePage):
    template_name = 'my_simple_survey/Joke1672.html'


class Joke1673(JokePage):
    template_name = 'my_simple_survey/Joke1673.html'


class Joke1674(JokePage):
    template_name = 'my_simple_survey/Joke1674.html'


class Joke1675(JokePage):
    template_name = 'my_simple_survey/Joke1675.html'


class Joke1676(JokePage):
    template_name = 'my_simple_survey/Joke1676.html'


class Joke1677(JokePage):
    template_name = 'my_simple_survey/Joke1677.html'


class Joke1678(JokePage):
    template_name = 'my_simple_survey/Joke1678.html'


class Joke1679(JokePage):
    template_name = 'my_simple_survey/Joke1679.html'


class Joke1680(JokePage):
    template_name = 'my_simple_survey/Joke1680.html'


class Joke1681(JokePage):
    template_name = 'my_simple_survey/Joke1681.html'


class Joke1682(JokePage):
    template_name = 'my_simple_survey/Joke1682.html'


class Joke1683(JokePage):
    template_name = 'my_simple_survey/Joke1683.html'


class Joke1684(JokePage):
    template_name = 'my_simple_survey/Joke1684.html'


class Joke1685(JokePage):
    template_name = 'my_simple_survey/Joke1685.html'


class Joke1686(JokePage):
    template_name = 'my_simple_survey/Joke1686.html'


class Joke1687(JokePage):
    template_name = 'my_simple_survey/Joke1687.html'


class Joke1688(JokePage):
    template_name = 'my_simple_survey/Joke1688.html'


class Joke1689(JokePage):
    template_name = 'my_simple_survey/Joke1689.html'


class Joke1690(JokePage):
    template_name = 'my_simple_survey/Joke1690.html'


class Joke1691(JokePage):
    template_name = 'my_simple_survey/Joke1691.html'


class Joke1692(JokePage):
    template_name = 'my_simple_survey/Joke1692.html'


class Joke1693(JokePage):
    template_name = 'my_simple_survey/Joke1693.html'


class Joke1694(JokePage):
    template_name = 'my_simple_survey/Joke1694.html'


class Joke1695(JokePage):
    template_name = 'my_simple_survey/Joke1695.html'


class Joke1696(JokePage):
    template_name = 'my_simple_survey/Joke1696.html'


class Joke1697(JokePage):
    template_name = 'my_simple_survey/Joke1697.html'


class Joke1698(JokePage):
    template_name = 'my_simple_survey/Joke1698.html'


class Joke1699(JokePage):
    template_name = 'my_simple_survey/Joke1699.html'


class Joke1700(JokePage):
    template_name = 'my_simple_survey/Joke1700.html'


class Joke1701(JokePage):
    template_name = 'my_simple_survey/Joke1701.html'


class Joke1702(JokePage):
    template_name = 'my_simple_survey/Joke1702.html'


class Joke1703(JokePage):
    template_name = 'my_simple_survey/Joke1703.html'


class Joke1704(JokePage):
    template_name = 'my_simple_survey/Joke1704.html'


class Joke1705(JokePage):
    template_name = 'my_simple_survey/Joke1705.html'


class Joke1706(JokePage):
    template_name = 'my_simple_survey/Joke1706.html'


class Joke1707(JokePage):
    template_name = 'my_simple_survey/Joke1707.html'


class Joke1708(JokePage):
    template_name = 'my_simple_survey/Joke1708.html'


class Joke1709(JokePage):
    template_name = 'my_simple_survey/Joke1709.html'


class Joke1710(JokePage):
    template_name = 'my_simple_survey/Joke1710.html'


class Joke1711(JokePage):
    template_name = 'my_simple_survey/Joke1711.html'


class Joke1712(JokePage):
    template_name = 'my_simple_survey/Joke1712.html'


class Joke1713(JokePage):
    template_name = 'my_simple_survey/Joke1713.html'


class Joke1714(JokePage):
    template_name = 'my_simple_survey/Joke1714.html'


class Joke1715(JokePage):
    template_name = 'my_simple_survey/Joke1715.html'


class Joke1716(JokePage):
    template_name = 'my_simple_survey/Joke1716.html'


class Joke1717(JokePage):
    template_name = 'my_simple_survey/Joke1717.html'


class Joke1718(JokePage):
    template_name = 'my_simple_survey/Joke1718.html'


class Joke1719(JokePage):
    template_name = 'my_simple_survey/Joke1719.html'


class Joke1720(JokePage):
    template_name = 'my_simple_survey/Joke1720.html'


class Joke1721(JokePage):
    template_name = 'my_simple_survey/Joke1721.html'


class Joke1722(JokePage):
    template_name = 'my_simple_survey/Joke1722.html'


class Joke1723(JokePage):
    template_name = 'my_simple_survey/Joke1723.html'


class Joke1724(JokePage):
    template_name = 'my_simple_survey/Joke1724.html'


class Joke1725(JokePage):
    template_name = 'my_simple_survey/Joke1725.html'


class Joke1726(JokePage):
    template_name = 'my_simple_survey/Joke1726.html'


class Joke1727(JokePage):
    template_name = 'my_simple_survey/Joke1727.html'


class Joke1728(JokePage):
    template_name = 'my_simple_survey/Joke1728.html'


class Joke1729(JokePage):
    template_name = 'my_simple_survey/Joke1729.html'


class Joke1730(JokePage):
    template_name = 'my_simple_survey/Joke1730.html'


class Joke1731(JokePage):
    template_name = 'my_simple_survey/Joke1731.html'


class Joke1732(JokePage):
    template_name = 'my_simple_survey/Joke1732.html'


class Joke1733(JokePage):
    template_name = 'my_simple_survey/Joke1733.html'


class Joke1734(JokePage):
    template_name = 'my_simple_survey/Joke1734.html'


class Joke1735(JokePage):
    template_name = 'my_simple_survey/Joke1735.html'


class Joke1736(JokePage):
    template_name = 'my_simple_survey/Joke1736.html'


class Joke1737(JokePage):
    template_name = 'my_simple_survey/Joke1737.html'


class Joke1738(JokePage):
    template_name = 'my_simple_survey/Joke1738.html'


class Joke1739(JokePage):
    template_name = 'my_simple_survey/Joke1739.html'


class Joke1740(JokePage):
    template_name = 'my_simple_survey/Joke1740.html'


class Joke1741(JokePage):
    template_name = 'my_simple_survey/Joke1741.html'


class Joke1742(JokePage):
    template_name = 'my_simple_survey/Joke1742.html'


class Joke1743(JokePage):
    template_name = 'my_simple_survey/Joke1743.html'


class Joke1744(JokePage):
    template_name = 'my_simple_survey/Joke1744.html'


class Joke1745(JokePage):
    template_name = 'my_simple_survey/Joke1745.html'


class Joke1746(JokePage):
    template_name = 'my_simple_survey/Joke1746.html'


class Joke1747(JokePage):
    template_name = 'my_simple_survey/Joke1747.html'


class Joke1748(JokePage):
    template_name = 'my_simple_survey/Joke1748.html'


class Joke1749(JokePage):
    template_name = 'my_simple_survey/Joke1749.html'


class Joke1750(JokePage):
    template_name = 'my_simple_survey/Joke1750.html'


class Joke1751(JokePage):
    template_name = 'my_simple_survey/Joke1751.html'


class Joke1752(JokePage):
    template_name = 'my_simple_survey/Joke1752.html'


class Joke1753(JokePage):
    template_name = 'my_simple_survey/Joke1753.html'


class Joke1754(JokePage):
    template_name = 'my_simple_survey/Joke1754.html'


class Joke1755(JokePage):
    template_name = 'my_simple_survey/Joke1755.html'


class Joke1756(JokePage):
    template_name = 'my_simple_survey/Joke1756.html'


class Joke1757(JokePage):
    template_name = 'my_simple_survey/Joke1757.html'


class Joke1758(JokePage):
    template_name = 'my_simple_survey/Joke1758.html'


class Joke1759(JokePage):
    template_name = 'my_simple_survey/Joke1759.html'


class Joke1760(JokePage):
    template_name = 'my_simple_survey/Joke1760.html'


class Joke1761(JokePage):
    template_name = 'my_simple_survey/Joke1761.html'


class Joke1762(JokePage):
    template_name = 'my_simple_survey/Joke1762.html'


class Joke1763(JokePage):
    template_name = 'my_simple_survey/Joke1763.html'


class Joke1764(JokePage):
    template_name = 'my_simple_survey/Joke1764.html'


class Joke1765(JokePage):
    template_name = 'my_simple_survey/Joke1765.html'


class Joke1766(JokePage):
    template_name = 'my_simple_survey/Joke1766.html'


class Joke1767(JokePage):
    template_name = 'my_simple_survey/Joke1767.html'


class Joke1768(JokePage):
    template_name = 'my_simple_survey/Joke1768.html'


class Joke1769(JokePage):
    template_name = 'my_simple_survey/Joke1769.html'


class Joke1770(JokePage):
    template_name = 'my_simple_survey/Joke1770.html'


class Joke1771(JokePage):
    template_name = 'my_simple_survey/Joke1771.html'


class Joke1772(JokePage):
    template_name = 'my_simple_survey/Joke1772.html'


class Joke1773(JokePage):
    template_name = 'my_simple_survey/Joke1773.html'


class Joke1774(JokePage):
    template_name = 'my_simple_survey/Joke1774.html'


class Joke1775(JokePage):
    template_name = 'my_simple_survey/Joke1775.html'


class Joke1776(JokePage):
    template_name = 'my_simple_survey/Joke1776.html'


class Joke1777(JokePage):
    template_name = 'my_simple_survey/Joke1777.html'


class Joke1778(JokePage):
    template_name = 'my_simple_survey/Joke1778.html'


class Joke1779(JokePage):
    template_name = 'my_simple_survey/Joke1779.html'


class Joke1780(JokePage):
    template_name = 'my_simple_survey/Joke1780.html'


class Joke1781(JokePage):
    template_name = 'my_simple_survey/Joke1781.html'


class Joke1782(JokePage):
    template_name = 'my_simple_survey/Joke1782.html'


class Joke1783(JokePage):
    template_name = 'my_simple_survey/Joke1783.html'


class Joke1784(JokePage):
    template_name = 'my_simple_survey/Joke1784.html'


class Joke1785(JokePage):
    template_name = 'my_simple_survey/Joke1785.html'


class Joke1786(JokePage):
    template_name = 'my_simple_survey/Joke1786.html'


class Joke1787(JokePage):
    template_name = 'my_simple_survey/Joke1787.html'


class Joke1788(JokePage):
    template_name = 'my_simple_survey/Joke1788.html'


class Joke1789(JokePage):
    template_name = 'my_simple_survey/Joke1789.html'


class Joke1790(JokePage):
    template_name = 'my_simple_survey/Joke1790.html'


class Joke1791(JokePage):
    template_name = 'my_simple_survey/Joke1791.html'


class Joke1792(JokePage):
    template_name = 'my_simple_survey/Joke1792.html'


class Joke1793(JokePage):
    template_name = 'my_simple_survey/Joke1793.html'


class Joke1794(JokePage):
    template_name = 'my_simple_survey/Joke1794.html'


class Joke1795(JokePage):
    template_name = 'my_simple_survey/Joke1795.html'


class Joke1796(JokePage):
    template_name = 'my_simple_survey/Joke1796.html'


class Joke1797(JokePage):
    template_name = 'my_simple_survey/Joke1797.html'


class Joke1798(JokePage):
    template_name = 'my_simple_survey/Joke1798.html'


class Joke1799(JokePage):
    template_name = 'my_simple_survey/Joke1799.html'


class Joke1800(JokePage):
    template_name = 'my_simple_survey/Joke1800.html'


class Joke1801(JokePage):
    template_name = 'my_simple_survey/Joke1801.html'


class Joke1802(JokePage):
    template_name = 'my_simple_survey/Joke1802.html'


class Joke1803(JokePage):
    template_name = 'my_simple_survey/Joke1803.html'


class Joke1804(JokePage):
    template_name = 'my_simple_survey/Joke1804.html'


class Joke1805(JokePage):
    template_name = 'my_simple_survey/Joke1805.html'


class Joke1806(JokePage):
    template_name = 'my_simple_survey/Joke1806.html'


class Joke1807(JokePage):
    template_name = 'my_simple_survey/Joke1807.html'


class Joke1808(JokePage):
    template_name = 'my_simple_survey/Joke1808.html'


class Joke1809(JokePage):
    template_name = 'my_simple_survey/Joke1809.html'


class Joke1810(JokePage):
    template_name = 'my_simple_survey/Joke1810.html'


class Joke1811(JokePage):
    template_name = 'my_simple_survey/Joke1811.html'


class Joke1812(JokePage):
    template_name = 'my_simple_survey/Joke1812.html'


class Joke1813(JokePage):
    template_name = 'my_simple_survey/Joke1813.html'


class Joke1814(JokePage):
    template_name = 'my_simple_survey/Joke1814.html'


class Joke1815(JokePage):
    template_name = 'my_simple_survey/Joke1815.html'


class Joke1816(JokePage):
    template_name = 'my_simple_survey/Joke1816.html'


class Joke1817(JokePage):
    template_name = 'my_simple_survey/Joke1817.html'


class Joke1818(JokePage):
    template_name = 'my_simple_survey/Joke1818.html'


class Joke1819(JokePage):
    template_name = 'my_simple_survey/Joke1819.html'


class Joke1820(JokePage):
    template_name = 'my_simple_survey/Joke1820.html'


class Joke1821(JokePage):
    template_name = 'my_simple_survey/Joke1821.html'


class Joke1822(JokePage):
    template_name = 'my_simple_survey/Joke1822.html'


class Joke1823(JokePage):
    template_name = 'my_simple_survey/Joke1823.html'


class Joke1824(JokePage):
    template_name = 'my_simple_survey/Joke1824.html'


class Joke1825(JokePage):
    template_name = 'my_simple_survey/Joke1825.html'


class Joke1826(JokePage):
    template_name = 'my_simple_survey/Joke1826.html'


class Joke1827(JokePage):
    template_name = 'my_simple_survey/Joke1827.html'


class Joke1828(JokePage):
    template_name = 'my_simple_survey/Joke1828.html'


class Joke1829(JokePage):
    template_name = 'my_simple_survey/Joke1829.html'


class Joke1830(JokePage):
    template_name = 'my_simple_survey/Joke1830.html'


class Joke1831(JokePage):
    template_name = 'my_simple_survey/Joke1831.html'


class Joke1832(JokePage):
    template_name = 'my_simple_survey/Joke1832.html'


class Joke1833(JokePage):
    template_name = 'my_simple_survey/Joke1833.html'


class Joke1834(JokePage):
    template_name = 'my_simple_survey/Joke1834.html'


class Joke1835(JokePage):
    template_name = 'my_simple_survey/Joke1835.html'


class Joke1836(JokePage):
    template_name = 'my_simple_survey/Joke1836.html'


class Joke1837(JokePage):
    template_name = 'my_simple_survey/Joke1837.html'


class Joke1838(JokePage):
    template_name = 'my_simple_survey/Joke1838.html'


class Joke1839(JokePage):
    template_name = 'my_simple_survey/Joke1839.html'


class Joke1840(JokePage):
    template_name = 'my_simple_survey/Joke1840.html'


class Joke1841(JokePage):
    template_name = 'my_simple_survey/Joke1841.html'


class Joke1842(JokePage):
    template_name = 'my_simple_survey/Joke1842.html'


class Joke1843(JokePage):
    template_name = 'my_simple_survey/Joke1843.html'


class Joke1844(JokePage):
    template_name = 'my_simple_survey/Joke1844.html'


class Joke1845(JokePage):
    template_name = 'my_simple_survey/Joke1845.html'


class Joke1846(JokePage):
    template_name = 'my_simple_survey/Joke1846.html'


class Joke1847(JokePage):
    template_name = 'my_simple_survey/Joke1847.html'


class Joke1848(JokePage):
    template_name = 'my_simple_survey/Joke1848.html'


class Joke1849(JokePage):
    template_name = 'my_simple_survey/Joke1849.html'


class Joke1850(JokePage):
    template_name = 'my_simple_survey/Joke1850.html'


class Joke1851(JokePage):
    template_name = 'my_simple_survey/Joke1851.html'


class Joke1852(JokePage):
    template_name = 'my_simple_survey/Joke1852.html'


class Joke1853(JokePage):
    template_name = 'my_simple_survey/Joke1853.html'


class Joke1854(JokePage):
    template_name = 'my_simple_survey/Joke1854.html'


class Joke1855(JokePage):
    template_name = 'my_simple_survey/Joke1855.html'


class Joke1856(JokePage):
    template_name = 'my_simple_survey/Joke1856.html'


class Joke1857(JokePage):
    template_name = 'my_simple_survey/Joke1857.html'


class Joke1858(JokePage):
    template_name = 'my_simple_survey/Joke1858.html'


class Joke1859(JokePage):
    template_name = 'my_simple_survey/Joke1859.html'


class Joke1860(JokePage):
    template_name = 'my_simple_survey/Joke1860.html'


class Joke1861(JokePage):
    template_name = 'my_simple_survey/Joke1861.html'


class Joke1862(JokePage):
    template_name = 'my_simple_survey/Joke1862.html'


class Joke1863(JokePage):
    template_name = 'my_simple_survey/Joke1863.html'


class Joke1864(JokePage):
    template_name = 'my_simple_survey/Joke1864.html'


class Joke1865(JokePage):
    template_name = 'my_simple_survey/Joke1865.html'


class Joke1866(JokePage):
    template_name = 'my_simple_survey/Joke1866.html'


class Joke1867(JokePage):
    template_name = 'my_simple_survey/Joke1867.html'


class Joke1868(JokePage):
    template_name = 'my_simple_survey/Joke1868.html'


class Joke1869(JokePage):
    template_name = 'my_simple_survey/Joke1869.html'


class Joke1870(JokePage):
    template_name = 'my_simple_survey/Joke1870.html'


class Joke1871(JokePage):
    template_name = 'my_simple_survey/Joke1871.html'


class Joke1872(JokePage):
    template_name = 'my_simple_survey/Joke1872.html'


class Joke1873(JokePage):
    template_name = 'my_simple_survey/Joke1873.html'


class Joke1874(JokePage):
    template_name = 'my_simple_survey/Joke1874.html'


class Joke1875(JokePage):
    template_name = 'my_simple_survey/Joke1875.html'


class Joke1876(JokePage):
    template_name = 'my_simple_survey/Joke1876.html'


class Joke1877(JokePage):
    template_name = 'my_simple_survey/Joke1877.html'


class Joke1878(JokePage):
    template_name = 'my_simple_survey/Joke1878.html'


class Joke1879(JokePage):
    template_name = 'my_simple_survey/Joke1879.html'


class Joke1880(JokePage):
    template_name = 'my_simple_survey/Joke1880.html'


class Joke1881(JokePage):
    template_name = 'my_simple_survey/Joke1881.html'


class Joke1882(JokePage):
    template_name = 'my_simple_survey/Joke1882.html'


class Joke1883(JokePage):
    template_name = 'my_simple_survey/Joke1883.html'


class Joke1884(JokePage):
    template_name = 'my_simple_survey/Joke1884.html'


class Joke1885(JokePage):
    template_name = 'my_simple_survey/Joke1885.html'


class Joke1886(JokePage):
    template_name = 'my_simple_survey/Joke1886.html'


class Joke1887(JokePage):
    template_name = 'my_simple_survey/Joke1887.html'


class Joke1888(JokePage):
    template_name = 'my_simple_survey/Joke1888.html'


class Joke1889(JokePage):
    template_name = 'my_simple_survey/Joke1889.html'


class Joke1890(JokePage):
    template_name = 'my_simple_survey/Joke1890.html'


class Joke1891(JokePage):
    template_name = 'my_simple_survey/Joke1891.html'


class Joke1892(JokePage):
    template_name = 'my_simple_survey/Joke1892.html'


class Joke1893(JokePage):
    template_name = 'my_simple_survey/Joke1893.html'


class Joke1894(JokePage):
    template_name = 'my_simple_survey/Joke1894.html'


class Joke1895(JokePage):
    template_name = 'my_simple_survey/Joke1895.html'


class Joke1896(JokePage):
    template_name = 'my_simple_survey/Joke1896.html'


class Joke1897(JokePage):
    template_name = 'my_simple_survey/Joke1897.html'


class Joke1898(JokePage):
    template_name = 'my_simple_survey/Joke1898.html'


class Joke1899(JokePage):
    template_name = 'my_simple_survey/Joke1899.html'


class Joke1900(JokePage):
    template_name = 'my_simple_survey/Joke1900.html'


class Joke1901(JokePage):
    template_name = 'my_simple_survey/Joke1901.html'


class Joke1902(JokePage):
    template_name = 'my_simple_survey/Joke1902.html'


class Joke1903(JokePage):
    template_name = 'my_simple_survey/Joke1903.html'


class Joke1904(JokePage):
    template_name = 'my_simple_survey/Joke1904.html'


class Joke1905(JokePage):
    template_name = 'my_simple_survey/Joke1905.html'


class Joke1906(JokePage):
    template_name = 'my_simple_survey/Joke1906.html'


class Joke1907(JokePage):
    template_name = 'my_simple_survey/Joke1907.html'


class Joke1908(JokePage):
    template_name = 'my_simple_survey/Joke1908.html'


class Joke1909(JokePage):
    template_name = 'my_simple_survey/Joke1909.html'


class Joke1910(JokePage):
    template_name = 'my_simple_survey/Joke1910.html'


class Joke1911(JokePage):
    template_name = 'my_simple_survey/Joke1911.html'


class Joke1912(JokePage):
    template_name = 'my_simple_survey/Joke1912.html'


class Joke1913(JokePage):
    template_name = 'my_simple_survey/Joke1913.html'


class Joke1914(JokePage):
    template_name = 'my_simple_survey/Joke1914.html'


class Joke1915(JokePage):
    template_name = 'my_simple_survey/Joke1915.html'


class Joke1916(JokePage):
    template_name = 'my_simple_survey/Joke1916.html'


class Joke1917(JokePage):
    template_name = 'my_simple_survey/Joke1917.html'


class Joke1918(JokePage):
    template_name = 'my_simple_survey/Joke1918.html'


class Joke1919(JokePage):
    template_name = 'my_simple_survey/Joke1919.html'


class Joke1920(JokePage):
    template_name = 'my_simple_survey/Joke1920.html'


class Joke1921(JokePage):
    template_name = 'my_simple_survey/Joke1921.html'


class Joke1922(JokePage):
    template_name = 'my_simple_survey/Joke1922.html'


class Joke1923(JokePage):
    template_name = 'my_simple_survey/Joke1923.html'


class Joke1924(JokePage):
    template_name = 'my_simple_survey/Joke1924.html'


class Joke1925(JokePage):
    template_name = 'my_simple_survey/Joke1925.html'


class Joke1926(JokePage):
    template_name = 'my_simple_survey/Joke1926.html'


class Joke1927(JokePage):
    template_name = 'my_simple_survey/Joke1927.html'


class Joke1928(JokePage):
    template_name = 'my_simple_survey/Joke1928.html'


class Joke1929(JokePage):
    template_name = 'my_simple_survey/Joke1929.html'


class Joke1930(JokePage):
    template_name = 'my_simple_survey/Joke1930.html'


class Joke1931(JokePage):
    template_name = 'my_simple_survey/Joke1931.html'


class Joke1932(JokePage):
    template_name = 'my_simple_survey/Joke1932.html'


class Joke1933(JokePage):
    template_name = 'my_simple_survey/Joke1933.html'


class Joke1934(JokePage):
    template_name = 'my_simple_survey/Joke1934.html'


class Joke1935(JokePage):
    template_name = 'my_simple_survey/Joke1935.html'


class Joke1936(JokePage):
    template_name = 'my_simple_survey/Joke1936.html'


class Joke1937(JokePage):
    template_name = 'my_simple_survey/Joke1937.html'


class Joke1938(JokePage):
    template_name = 'my_simple_survey/Joke1938.html'


class Joke1939(JokePage):
    template_name = 'my_simple_survey/Joke1939.html'


class Joke1940(JokePage):
    template_name = 'my_simple_survey/Joke1940.html'


class Joke1941(JokePage):
    template_name = 'my_simple_survey/Joke1941.html'


class Joke1942(JokePage):
    template_name = 'my_simple_survey/Joke1942.html'


class Joke1943(JokePage):
    template_name = 'my_simple_survey/Joke1943.html'


class Joke1944(JokePage):
    template_name = 'my_simple_survey/Joke1944.html'


class Joke1945(JokePage):
    template_name = 'my_simple_survey/Joke1945.html'


class Joke1946(JokePage):
    template_name = 'my_simple_survey/Joke1946.html'


class Joke1947(JokePage):
    template_name = 'my_simple_survey/Joke1947.html'


class Joke1948(JokePage):
    template_name = 'my_simple_survey/Joke1948.html'


class Joke1949(JokePage):
    template_name = 'my_simple_survey/Joke1949.html'


class Joke1950(JokePage):
    template_name = 'my_simple_survey/Joke1950.html'


class Joke1951(JokePage):
    template_name = 'my_simple_survey/Joke1951.html'


class Joke1952(JokePage):
    template_name = 'my_simple_survey/Joke1952.html'


class Joke1953(JokePage):
    template_name = 'my_simple_survey/Joke1953.html'


class Joke1954(JokePage):
    template_name = 'my_simple_survey/Joke1954.html'


class Joke1955(JokePage):
    template_name = 'my_simple_survey/Joke1955.html'


class Joke1956(JokePage):
    template_name = 'my_simple_survey/Joke1956.html'


class Joke1957(JokePage):
    template_name = 'my_simple_survey/Joke1957.html'


class Joke1958(JokePage):
    template_name = 'my_simple_survey/Joke1958.html'


class Joke1959(JokePage):
    template_name = 'my_simple_survey/Joke1959.html'


class Joke1960(JokePage):
    template_name = 'my_simple_survey/Joke1960.html'


class Joke1961(JokePage):
    template_name = 'my_simple_survey/Joke1961.html'


class Joke1962(JokePage):
    template_name = 'my_simple_survey/Joke1962.html'


class Joke1963(JokePage):
    template_name = 'my_simple_survey/Joke1963.html'


class Joke1964(JokePage):
    template_name = 'my_simple_survey/Joke1964.html'


class Joke1965(JokePage):
    template_name = 'my_simple_survey/Joke1965.html'


class Joke1966(JokePage):
    template_name = 'my_simple_survey/Joke1966.html'


class Joke1967(JokePage):
    template_name = 'my_simple_survey/Joke1967.html'


class Joke1968(JokePage):
    template_name = 'my_simple_survey/Joke1968.html'


class Joke1969(JokePage):
    template_name = 'my_simple_survey/Joke1969.html'


class Joke1970(JokePage):
    template_name = 'my_simple_survey/Joke1970.html'


class Joke1971(JokePage):
    template_name = 'my_simple_survey/Joke1971.html'


class Joke1972(JokePage):
    template_name = 'my_simple_survey/Joke1972.html'


class Joke1973(JokePage):
    template_name = 'my_simple_survey/Joke1973.html'


class Joke1974(JokePage):
    template_name = 'my_simple_survey/Joke1974.html'


class Joke1975(JokePage):
    template_name = 'my_simple_survey/Joke1975.html'


class Joke1976(JokePage):
    template_name = 'my_simple_survey/Joke1976.html'


class Joke1977(JokePage):
    template_name = 'my_simple_survey/Joke1977.html'


class Joke1978(JokePage):
    template_name = 'my_simple_survey/Joke1978.html'


class Joke1979(JokePage):
    template_name = 'my_simple_survey/Joke1979.html'


class Joke1980(JokePage):
    template_name = 'my_simple_survey/Joke1980.html'


class Joke1981(JokePage):
    template_name = 'my_simple_survey/Joke1981.html'


class Joke1982(JokePage):
    template_name = 'my_simple_survey/Joke1982.html'


class Joke1983(JokePage):
    template_name = 'my_simple_survey/Joke1983.html'


class Joke1984(JokePage):
    template_name = 'my_simple_survey/Joke1984.html'


class Joke1985(JokePage):
    template_name = 'my_simple_survey/Joke1985.html'


class Joke1986(JokePage):
    template_name = 'my_simple_survey/Joke1986.html'


class Joke1987(JokePage):
    template_name = 'my_simple_survey/Joke1987.html'


class Joke1988(JokePage):
    template_name = 'my_simple_survey/Joke1988.html'


class Joke1989(JokePage):
    template_name = 'my_simple_survey/Joke1989.html'


class Joke1990(JokePage):
    template_name = 'my_simple_survey/Joke1990.html'


class Joke1991(JokePage):
    template_name = 'my_simple_survey/Joke1991.html'


class Joke1992(JokePage):
    template_name = 'my_simple_survey/Joke1992.html'


class Joke1993(JokePage):
    template_name = 'my_simple_survey/Joke1993.html'


class Joke1994(JokePage):
    template_name = 'my_simple_survey/Joke1994.html'


class Joke1995(JokePage):
    template_name = 'my_simple_survey/Joke1995.html'


class Joke1996(JokePage):
    template_name = 'my_simple_survey/Joke1996.html'


class Joke1997(JokePage):
    template_name = 'my_simple_survey/Joke1997.html'


class Joke1998(JokePage):
    template_name = 'my_simple_survey/Joke1998.html'


class Joke1999(JokePage):
    template_name = 'my_simple_survey/Joke1999.html'


class Joke2000(JokePage):
    template_name = 'my_simple_survey/Joke2000.html'


page_sequence = [
    Preview,
    Joke1,
    Joke2,
    Joke3,
    Joke4,
    Joke5,
    Joke6,
    Joke7,
    Joke8,
    Joke9,
    Joke10,
    Joke11,
    Joke12,
    Joke13,
    Joke14,
    Joke15,
    Joke16,
    Joke17,
    Joke18,
    Joke19,
    Joke20,
    Joke21,
    Joke22,
    Joke23,
    Joke24,
    Joke25,
    Joke26,
    Joke27,
    Joke28,
    Joke29,
    Joke30,
    Joke31,
    Joke32,
    Joke33,
    Joke34,
    Joke35,
    Joke36,
    Joke37,
    Joke38,
    Joke39,
    Joke40,
    Joke41,
    Joke42,
    Joke43,
    Joke44,
    Joke45,
    Joke46,
    Joke47,
    Joke48,
    Joke49,
    Joke50,
    Joke51,
    Joke52,
    Joke53,
    Joke54,
    Joke55,
    Joke56,
    Joke57,
    Joke58,
    Joke59,
    Joke60,
    Joke61,
    Joke62,
    Joke63,
    Joke64,
    Joke65,
    Joke66,
    Joke67,
    Joke68,
    Joke69,
    Joke70,
    Joke71,
    Joke72,
    Joke73,
    Joke74,
    Joke75,
    Joke76,
    Joke77,
    Joke78,
    Joke79,
    Joke80,
    Joke81,
    Joke82,
    Joke83,
    Joke84,
    Joke85,
    Joke86,
    Joke87,
    Joke88,
    Joke89,
    Joke90,
    Joke91,
    Joke92,
    Joke93,
    Joke94,
    Joke95,
    Joke96,
    Joke97,
    Joke98,
    Joke99,
    Joke100,
    Joke101,
    Joke102,
    Joke103,
    Joke104,
    Joke105,
    Joke106,
    Joke107,
    Joke108,
    Joke109,
    Joke110,
    Joke111,
    Joke112,
    Joke113,
    Joke114,
    Joke115,
    Joke116,
    Joke117,
    Joke118,
    Joke119,
    Joke120,
    Joke121,
    Joke122,
    Joke123,
    Joke124,
    Joke125,
    Joke126,
    Joke127,
    Joke128,
    Joke129,
    Joke130,
    Joke131,
    Joke132,
    Joke133,
    Joke134,
    Joke135,
    Joke136,
    Joke137,
    Joke138,
    Joke139,
    Joke140,
    Joke141,
    Joke142,
    Joke143,
    Joke144,
    Joke145,
    Joke146,
    Joke147,
    Joke148,
    Joke149,
    Joke150,
    Joke151,
    Joke152,
    Joke153,
    Joke154,
    Joke155,
    Joke156,
    Joke157,
    Joke158,
    Joke159,
    Joke160,
    Joke161,
    Joke162,
    Joke163,
    Joke164,
    Joke165,
    Joke166,
    Joke167,
    Joke168,
    Joke169,
    Joke170,
    Joke171,
    Joke172,
    Joke173,
    Joke174,
    Joke175,
    Joke176,
    Joke177,
    Joke178,
    Joke179,
    Joke180,
    Joke181,
    Joke182,
    Joke183,
    Joke184,
    Joke185,
    Joke186,
    Joke187,
    Joke188,
    Joke189,
    Joke190,
    Joke191,
    Joke192,
    Joke193,
    Joke194,
    Joke195,
    Joke196,
    Joke197,
    Joke198,
    Joke199,
    Joke200,
    Joke201,
    Joke202,
    Joke203,
    Joke204,
    Joke205,
    Joke206,
    Joke207,
    Joke208,
    Joke209,
    Joke210,
    Joke211,
    Joke212,
    Joke213,
    Joke214,
    Joke215,
    Joke216,
    Joke217,
    Joke218,
    Joke219,
    Joke220,
    Joke221,
    Joke222,
    Joke223,
    Joke224,
    Joke225,
    Joke226,
    Joke227,
    Joke228,
    Joke229,
    Joke230,
    Joke231,
    Joke232,
    Joke233,
    Joke234,
    Joke235,
    Joke236,
    Joke237,
    Joke238,
    Joke239,
    Joke240,
    Joke241,
    Joke242,
    Joke243,
    Joke244,
    Joke245,
    Joke246,
    Joke247,
    Joke248,
    Joke249,
    Joke250,
    Joke251,
    Joke252,
    Joke253,
    Joke254,
    Joke255,
    Joke256,
    Joke257,
    Joke258,
    Joke259,
    Joke260,
    Joke261,
    Joke262,
    Joke263,
    Joke264,
    Joke265,
    Joke266,
    Joke267,
    Joke268,
    Joke269,
    Joke270,
    Joke271,
    Joke272,
    Joke273,
    Joke274,
    Joke275,
    Joke276,
    Joke277,
    Joke278,
    Joke279,
    Joke280,
    Joke281,
    Joke282,
    Joke283,
    Joke284,
    Joke285,
    Joke286,
    Joke287,
    Joke288,
    Joke289,
    Joke290,
    Joke291,
    Joke292,
    Joke293,
    Joke294,
    Joke295,
    Joke296,
    Joke297,
    Joke298,
    Joke299,
    Joke300,
    Joke301,
    Joke302,
    Joke303,
    Joke304,
    Joke305,
    Joke306,
    Joke307,
    Joke308,
    Joke309,
    Joke310,
    Joke311,
    Joke312,
    Joke313,
    Joke314,
    Joke315,
    Joke316,
    Joke317,
    Joke318,
    Joke319,
    Joke320,
    Joke321,
    Joke322,
    Joke323,
    Joke324,
    Joke325,
    Joke326,
    Joke327,
    Joke328,
    Joke329,
    Joke330,
    Joke331,
    Joke332,
    Joke333,
    Joke334,
    Joke335,
    Joke336,
    Joke337,
    Joke338,
    Joke339,
    Joke340,
    Joke341,
    Joke342,
    Joke343,
    Joke344,
    Joke345,
    Joke346,
    Joke347,
    Joke348,
    Joke349,
    Joke350,
    Joke351,
    Joke352,
    Joke353,
    Joke354,
    Joke355,
    Joke356,
    Joke357,
    Joke358,
    Joke359,
    Joke360,
    Joke361,
    Joke362,
    Joke363,
    Joke364,
    Joke365,
    Joke366,
    Joke367,
    Joke368,
    Joke369,
    Joke370,
    Joke371,
    Joke372,
    Joke373,
    Joke374,
    Joke375,
    Joke376,
    Joke377,
    Joke378,
    Joke379,
    Joke380,
    Joke381,
    Joke382,
    Joke383,
    Joke384,
    Joke385,
    Joke386,
    Joke387,
    Joke388,
    Joke389,
    Joke390,
    Joke391,
    Joke392,
    Joke393,
    Joke394,
    Joke395,
    Joke396,
    Joke397,
    Joke398,
    Joke399,
    Joke400,
    Joke401,
    Joke402,
    Joke403,
    Joke404,
    Joke405,
    Joke406,
    Joke407,
    Joke408,
    Joke409,
    Joke410,
    Joke411,
    Joke412,
    Joke413,
    Joke414,
    Joke415,
    Joke416,
    Joke417,
    Joke418,
    Joke419,
    Joke420,
    Joke421,
    Joke422,
    Joke423,
    Joke424,
    Joke425,
    Joke426,
    Joke427,
    Joke428,
    Joke429,
    Joke430,
    Joke431,
    Joke432,
    Joke433,
    Joke434,
    Joke435,
    Joke436,
    Joke437,
    Joke438,
    Joke439,
    Joke440,
    Joke441,
    Joke442,
    Joke443,
    Joke444,
    Joke445,
    Joke446,
    Joke447,
    Joke448,
    Joke449,
    Joke450,
    Joke451,
    Joke452,
    Joke453,
    Joke454,
    Joke455,
    Joke456,
    Joke457,
    Joke458,
    Joke459,
    Joke460,
    Joke461,
    Joke462,
    Joke463,
    Joke464,
    Joke465,
    Joke466,
    Joke467,
    Joke468,
    Joke469,
    Joke470,
    Joke471,
    Joke472,
    Joke473,
    Joke474,
    Joke475,
    Joke476,
    Joke477,
    Joke478,
    Joke479,
    Joke480,
    Joke481,
    Joke482,
    Joke483,
    Joke484,
    Joke485,
    Joke486,
    Joke487,
    Joke488,
    Joke489,
    Joke490,
    Joke491,
    Joke492,
    Joke493,
    Joke494,
    Joke495,
    Joke496,
    Joke497,
    Joke498,
    Joke499,
    Joke500,
    Joke501,
    Joke502,
    Joke503,
    Joke504,
    Joke505,
    Joke506,
    Joke507,
    Joke508,
    Joke509,
    Joke510,
    Joke511,
    Joke512,
    Joke513,
    Joke514,
    Joke515,
    Joke516,
    Joke517,
    Joke518,
    Joke519,
    Joke520,
    Joke521,
    Joke522,
    Joke523,
    Joke524,
    Joke525,
    Joke526,
    Joke527,
    Joke528,
    Joke529,
    Joke530,
    Joke531,
    Joke532,
    Joke533,
    Joke534,
    Joke535,
    Joke536,
    Joke537,
    Joke538,
    Joke539,
    Joke540,
    Joke541,
    Joke542,
    Joke543,
    Joke544,
    Joke545,
    Joke546,
    Joke547,
    Joke548,
    Joke549,
    Joke550,
    Joke551,
    Joke552,
    Joke553,
    Joke554,
    Joke555,
    Joke556,
    Joke557,
    Joke558,
    Joke559,
    Joke560,
    Joke561,
    Joke562,
    Joke563,
    Joke564,
    Joke565,
    Joke566,
    Joke567,
    Joke568,
    Joke569,
    Joke570,
    Joke571,
    Joke572,
    Joke573,
    Joke574,
    Joke575,
    Joke576,
    Joke577,
    Joke578,
    Joke579,
    Joke580,
    Joke581,
    Joke582,
    Joke583,
    Joke584,
    Joke585,
    Joke586,
    Joke587,
    Joke588,
    Joke589,
    Joke590,
    Joke591,
    Joke592,
    Joke593,
    Joke594,
    Joke595,
    Joke596,
    Joke597,
    Joke598,
    Joke599,
    Joke600,
    Joke601,
    Joke602,
    Joke603,
    Joke604,
    Joke605,
    Joke606,
    Joke607,
    Joke608,
    Joke609,
    Joke610,
    Joke611,
    Joke612,
    Joke613,
    Joke614,
    Joke615,
    Joke616,
    Joke617,
    Joke618,
    Joke619,
    Joke620,
    Joke621,
    Joke622,
    Joke623,
    Joke624,
    Joke625,
    Joke626,
    Joke627,
    Joke628,
    Joke629,
    Joke630,
    Joke631,
    Joke632,
    Joke633,
    Joke634,
    Joke635,
    Joke636,
    Joke637,
    Joke638,
    Joke639,
    Joke640,
    Joke641,
    Joke642,
    Joke643,
    Joke644,
    Joke645,
    Joke646,
    Joke647,
    Joke648,
    Joke649,
    Joke650,
    Joke651,
    Joke652,
    Joke653,
    Joke654,
    Joke655,
    Joke656,
    Joke657,
    Joke658,
    Joke659,
    Joke660,
    Joke661,
    Joke662,
    Joke663,
    Joke664,
    Joke665,
    Joke666,
    Joke667,
    Joke668,
    Joke669,
    Joke670,
    Joke671,
    Joke672,
    Joke673,
    Joke674,
    Joke675,
    Joke676,
    Joke677,
    Joke678,
    Joke679,
    Joke680,
    Joke681,
    Joke682,
    Joke683,
    Joke684,
    Joke685,
    Joke686,
    Joke687,
    Joke688,
    Joke689,
    Joke690,
    Joke691,
    Joke692,
    Joke693,
    Joke694,
    Joke695,
    Joke696,
    Joke697,
    Joke698,
    Joke699,
    Joke700,
    Joke701,
    Joke702,
    Joke703,
    Joke704,
    Joke705,
    Joke706,
    Joke707,
    Joke708,
    Joke709,
    Joke710,
    Joke711,
    Joke712,
    Joke713,
    Joke714,
    Joke715,
    Joke716,
    Joke717,
    Joke718,
    Joke719,
    Joke720,
    Joke721,
    Joke722,
    Joke723,
    Joke724,
    Joke725,
    Joke726,
    Joke727,
    Joke728,
    Joke729,
    Joke730,
    Joke731,
    Joke732,
    Joke733,
    Joke734,
    Joke735,
    Joke736,
    Joke737,
    Joke738,
    Joke739,
    Joke740,
    Joke741,
    Joke742,
    Joke743,
    Joke744,
    Joke745,
    Joke746,
    Joke747,
    Joke748,
    Joke749,
    Joke750,
    Joke751,
    Joke752,
    Joke753,
    Joke754,
    Joke755,
    Joke756,
    Joke757,
    Joke758,
    Joke759,
    Joke760,
    Joke761,
    Joke762,
    Joke763,
    Joke764,
    Joke765,
    Joke766,
    Joke767,
    Joke768,
    Joke769,
    Joke770,
    Joke771,
    Joke772,
    Joke773,
    Joke774,
    Joke775,
    Joke776,
    Joke777,
    Joke778,
    Joke779,
    Joke780,
    Joke781,
    Joke782,
    Joke783,
    Joke784,
    Joke785,
    Joke786,
    Joke787,
    Joke788,
    Joke789,
    Joke790,
    Joke791,
    Joke792,
    Joke793,
    Joke794,
    Joke795,
    Joke796,
    Joke797,
    Joke798,
    Joke799,
    Joke800,
    Joke801,
    Joke802,
    Joke803,
    Joke804,
    Joke805,
    Joke806,
    Joke807,
    Joke808,
    Joke809,
    Joke810,
    Joke811,
    Joke812,
    Joke813,
    Joke814,
    Joke815,
    Joke816,
    Joke817,
    Joke818,
    Joke819,
    Joke820,
    Joke821,
    Joke822,
    Joke823,
    Joke824,
    Joke825,
    Joke826,
    Joke827,
    Joke828,
    Joke829,
    Joke830,
    Joke831,
    Joke832,
    Joke833,
    Joke834,
    Joke835,
    Joke836,
    Joke837,
    Joke838,
    Joke839,
    Joke840,
    Joke841,
    Joke842,
    Joke843,
    Joke844,
    Joke845,
    Joke846,
    Joke847,
    Joke848,
    Joke849,
    Joke850,
    Joke851,
    Joke852,
    Joke853,
    Joke854,
    Joke855,
    Joke856,
    Joke857,
    Joke858,
    Joke859,
    Joke860,
    Joke861,
    Joke862,
    Joke863,
    Joke864,
    Joke865,
    Joke866,
    Joke867,
    Joke868,
    Joke869,
    Joke870,
    Joke871,
    Joke872,
    Joke873,
    Joke874,
    Joke875,
    Joke876,
    Joke877,
    Joke878,
    Joke879,
    Joke880,
    Joke881,
    Joke882,
    Joke883,
    Joke884,
    Joke885,
    Joke886,
    Joke887,
    Joke888,
    Joke889,
    Joke890,
    Joke891,
    Joke892,
    Joke893,
    Joke894,
    Joke895,
    Joke896,
    Joke897,
    Joke898,
    Joke899,
    Joke900,
    Joke901,
    Joke902,
    Joke903,
    Joke904,
    Joke905,
    Joke906,
    Joke907,
    Joke908,
    Joke909,
    Joke910,
    Joke911,
    Joke912,
    Joke913,
    Joke914,
    Joke915,
    Joke916,
    Joke917,
    Joke918,
    Joke919,
    Joke920,
    Joke921,
    Joke922,
    Joke923,
    Joke924,
    Joke925,
    Joke926,
    Joke927,
    Joke928,
    Joke929,
    Joke930,
    Joke931,
    Joke932,
    Joke933,
    Joke934,
    Joke935,
    Joke936,
    Joke937,
    Joke938,
    Joke939,
    Joke940,
    Joke941,
    Joke942,
    Joke943,
    Joke944,
    Joke945,
    Joke946,
    Joke947,
    Joke948,
    Joke949,
    Joke950,
    Joke951,
    Joke952,
    Joke953,
    Joke954,
    Joke955,
    Joke956,
    Joke957,
    Joke958,
    Joke959,
    Joke960,
    Joke961,
    Joke962,
    Joke963,
    Joke964,
    Joke965,
    Joke966,
    Joke967,
    Joke968,
    Joke969,
    Joke970,
    Joke971,
    Joke972,
    Joke973,
    Joke974,
    Joke975,
    Joke976,
    Joke977,
    Joke978,
    Joke979,
    Joke980,
    Joke981,
    Joke982,
    Joke983,
    Joke984,
    Joke985,
    Joke986,
    Joke987,
    Joke988,
    Joke989,
    Joke990,
    Joke991,
    Joke992,
    Joke993,
    Joke994,
    Joke995,
    Joke996,
    Joke997,
    Joke998,
    Joke999,
    Joke1000,
    Joke1001,
    Joke1002,
    Joke1003,
    Joke1004,
    Joke1005,
    Joke1006,
    Joke1007,
    Joke1008,
    Joke1009,
    Joke1010,
    Joke1011,
    Joke1012,
    Joke1013,
    Joke1014,
    Joke1015,
    Joke1016,
    Joke1017,
    Joke1018,
    Joke1019,
    Joke1020,
    Joke1021,
    Joke1022,
    Joke1023,
    Joke1024,
    Joke1025,
    Joke1026,
    Joke1027,
    Joke1028,
    Joke1029,
    Joke1030,
    Joke1031,
    Joke1032,
    Joke1033,
    Joke1034,
    Joke1035,
    Joke1036,
    Joke1037,
    Joke1038,
    Joke1039,
    Joke1040,
    Joke1041,
    Joke1042,
    Joke1043,
    Joke1044,
    Joke1045,
    Joke1046,
    Joke1047,
    Joke1048,
    Joke1049,
    Joke1050,
    Joke1051,
    Joke1052,
    Joke1053,
    Joke1054,
    Joke1055,
    Joke1056,
    Joke1057,
    Joke1058,
    Joke1059,
    Joke1060,
    Joke1061,
    Joke1062,
    Joke1063,
    Joke1064,
    Joke1065,
    Joke1066,
    Joke1067,
    Joke1068,
    Joke1069,
    Joke1070,
    Joke1071,
    Joke1072,
    Joke1073,
    Joke1074,
    Joke1075,
    Joke1076,
    Joke1077,
    Joke1078,
    Joke1079,
    Joke1080,
    Joke1081,
    Joke1082,
    Joke1083,
    Joke1084,
    Joke1085,
    Joke1086,
    Joke1087,
    Joke1088,
    Joke1089,
    Joke1090,
    Joke1091,
    Joke1092,
    Joke1093,
    Joke1094,
    Joke1095,
    Joke1096,
    Joke1097,
    Joke1098,
    Joke1099,
    Joke1100,
    Joke1101,
    Joke1102,
    Joke1103,
    Joke1104,
    Joke1105,
    Joke1106,
    Joke1107,
    Joke1108,
    Joke1109,
    Joke1110,
    Joke1111,
    Joke1112,
    Joke1113,
    Joke1114,
    Joke1115,
    Joke1116,
    Joke1117,
    Joke1118,
    Joke1119,
    Joke1120,
    Joke1121,
    Joke1122,
    Joke1123,
    Joke1124,
    Joke1125,
    Joke1126,
    Joke1127,
    Joke1128,
    Joke1129,
    Joke1130,
    Joke1131,
    Joke1132,
    Joke1133,
    Joke1134,
    Joke1135,
    Joke1136,
    Joke1137,
    Joke1138,
    Joke1139,
    Joke1140,
    Joke1141,
    Joke1142,
    Joke1143,
    Joke1144,
    Joke1145,
    Joke1146,
    Joke1147,
    Joke1148,
    Joke1149,
    Joke1150,
    Joke1151,
    Joke1152,
    Joke1153,
    Joke1154,
    Joke1155,
    Joke1156,
    Joke1157,
    Joke1158,
    Joke1159,
    Joke1160,
    Joke1161,
    Joke1162,
    Joke1163,
    Joke1164,
    Joke1165,
    Joke1166,
    Joke1167,
    Joke1168,
    Joke1169,
    Joke1170,
    Joke1171,
    Joke1172,
    Joke1173,
    Joke1174,
    Joke1175,
    Joke1176,
    Joke1177,
    Joke1178,
    Joke1179,
    Joke1180,
    Joke1181,
    Joke1182,
    Joke1183,
    Joke1184,
    Joke1185,
    Joke1186,
    Joke1187,
    Joke1188,
    Joke1189,
    Joke1190,
    Joke1191,
    Joke1192,
    Joke1193,
    Joke1194,
    Joke1195,
    Joke1196,
    Joke1197,
    Joke1198,
    Joke1199,
    Joke1200,
    Joke1201,
    Joke1202,
    Joke1203,
    Joke1204,
    Joke1205,
    Joke1206,
    Joke1207,
    Joke1208,
    Joke1209,
    Joke1210,
    Joke1211,
    Joke1212,
    Joke1213,
    Joke1214,
    Joke1215,
    Joke1216,
    Joke1217,
    Joke1218,
    Joke1219,
    Joke1220,
    Joke1221,
    Joke1222,
    Joke1223,
    Joke1224,
    Joke1225,
    Joke1226,
    Joke1227,
    Joke1228,
    Joke1229,
    Joke1230,
    Joke1231,
    Joke1232,
    Joke1233,
    Joke1234,
    Joke1235,
    Joke1236,
    Joke1237,
    Joke1238,
    Joke1239,
    Joke1240,
    Joke1241,
    Joke1242,
    Joke1243,
    Joke1244,
    Joke1245,
    Joke1246,
    Joke1247,
    Joke1248,
    Joke1249,
    Joke1250,
    Joke1251,
    Joke1252,
    Joke1253,
    Joke1254,
    Joke1255,
    Joke1256,
    Joke1257,
    Joke1258,
    Joke1259,
    Joke1260,
    Joke1261,
    Joke1262,
    Joke1263,
    Joke1264,
    Joke1265,
    Joke1266,
    Joke1267,
    Joke1268,
    Joke1269,
    Joke1270,
    Joke1271,
    Joke1272,
    Joke1273,
    Joke1274,
    Joke1275,
    Joke1276,
    Joke1277,
    Joke1278,
    Joke1279,
    Joke1280,
    Joke1281,
    Joke1282,
    Joke1283,
    Joke1284,
    Joke1285,
    Joke1286,
    Joke1287,
    Joke1288,
    Joke1289,
    Joke1290,
    Joke1291,
    Joke1292,
    Joke1293,
    Joke1294,
    Joke1295,
    Joke1296,
    Joke1297,
    Joke1298,
    Joke1299,
    Joke1300,
    Joke1301,
    Joke1302,
    Joke1303,
    Joke1304,
    Joke1305,
    Joke1306,
    Joke1307,
    Joke1308,
    Joke1309,
    Joke1310,
    Joke1311,
    Joke1312,
    Joke1313,
    Joke1314,
    Joke1315,
    Joke1316,
    Joke1317,
    Joke1318,
    Joke1319,
    Joke1320,
    Joke1321,
    Joke1322,
    Joke1323,
    Joke1324,
    Joke1325,
    Joke1326,
    Joke1327,
    Joke1328,
    Joke1329,
    Joke1330,
    Joke1331,
    Joke1332,
    Joke1333,
    Joke1334,
    Joke1335,
    Joke1336,
    Joke1337,
    Joke1338,
    Joke1339,
    Joke1340,
    Joke1341,
    Joke1342,
    Joke1343,
    Joke1344,
    Joke1345,
    Joke1346,
    Joke1347,
    Joke1348,
    Joke1349,
    Joke1350,
    Joke1351,
    Joke1352,
    Joke1353,
    Joke1354,
    Joke1355,
    Joke1356,
    Joke1357,
    Joke1358,
    Joke1359,
    Joke1360,
    Joke1361,
    Joke1362,
    Joke1363,
    Joke1364,
    Joke1365,
    Joke1366,
    Joke1367,
    Joke1368,
    Joke1369,
    Joke1370,
    Joke1371,
    Joke1372,
    Joke1373,
    Joke1374,
    Joke1375,
    Joke1376,
    Joke1377,
    Joke1378,
    Joke1379,
    Joke1380,
    Joke1381,
    Joke1382,
    Joke1383,
    Joke1384,
    Joke1385,
    Joke1386,
    Joke1387,
    Joke1388,
    Joke1389,
    Joke1390,
    Joke1391,
    Joke1392,
    Joke1393,
    Joke1394,
    Joke1395,
    Joke1396,
    Joke1397,
    Joke1398,
    Joke1399,
    Joke1400,
    Joke1401,
    Joke1402,
    Joke1403,
    Joke1404,
    Joke1405,
    Joke1406,
    Joke1407,
    Joke1408,
    Joke1409,
    Joke1410,
    Joke1411,
    Joke1412,
    Joke1413,
    Joke1414,
    Joke1415,
    Joke1416,
    Joke1417,
    Joke1418,
    Joke1419,
    Joke1420,
    Joke1421,
    Joke1422,
    Joke1423,
    Joke1424,
    Joke1425,
    Joke1426,
    Joke1427,
    Joke1428,
    Joke1429,
    Joke1430,
    Joke1431,
    Joke1432,
    Joke1433,
    Joke1434,
    Joke1435,
    Joke1436,
    Joke1437,
    Joke1438,
    Joke1439,
    Joke1440,
    Joke1441,
    Joke1442,
    Joke1443,
    Joke1444,
    Joke1445,
    Joke1446,
    Joke1447,
    Joke1448,
    Joke1449,
    Joke1450,
    Joke1451,
    Joke1452,
    Joke1453,
    Joke1454,
    Joke1455,
    Joke1456,
    Joke1457,
    Joke1458,
    Joke1459,
    Joke1460,
    Joke1461,
    Joke1462,
    Joke1463,
    Joke1464,
    Joke1465,
    Joke1466,
    Joke1467,
    Joke1468,
    Joke1469,
    Joke1470,
    Joke1471,
    Joke1472,
    Joke1473,
    Joke1474,
    Joke1475,
    Joke1476,
    Joke1477,
    Joke1478,
    Joke1479,
    Joke1480,
    Joke1481,
    Joke1482,
    Joke1483,
    Joke1484,
    Joke1485,
    Joke1486,
    Joke1487,
    Joke1488,
    Joke1489,
    Joke1490,
    Joke1491,
    Joke1492,
    Joke1493,
    Joke1494,
    Joke1495,
    Joke1496,
    Joke1497,
    Joke1498,
    Joke1499,
    Joke1500,
    Joke1501,
    Joke1502,
    Joke1503,
    Joke1504,
    Joke1505,
    Joke1506,
    Joke1507,
    Joke1508,
    Joke1509,
    Joke1510,
    Joke1511,
    Joke1512,
    Joke1513,
    Joke1514,
    Joke1515,
    Joke1516,
    Joke1517,
    Joke1518,
    Joke1519,
    Joke1520,
    Joke1521,
    Joke1522,
    Joke1523,
    Joke1524,
    Joke1525,
    Joke1526,
    Joke1527,
    Joke1528,
    Joke1529,
    Joke1530,
    Joke1531,
    Joke1532,
    Joke1533,
    Joke1534,
    Joke1535,
    Joke1536,
    Joke1537,
    Joke1538,
    Joke1539,
    Joke1540,
    Joke1541,
    Joke1542,
    Joke1543,
    Joke1544,
    Joke1545,
    Joke1546,
    Joke1547,
    Joke1548,
    Joke1549,
    Joke1550,
    Joke1551,
    Joke1552,
    Joke1553,
    Joke1554,
    Joke1555,
    Joke1556,
    Joke1557,
    Joke1558,
    Joke1559,
    Joke1560,
    Joke1561,
    Joke1562,
    Joke1563,
    Joke1564,
    Joke1565,
    Joke1566,
    Joke1567,
    Joke1568,
    Joke1569,
    Joke1570,
    Joke1571,
    Joke1572,
    Joke1573,
    Joke1574,
    Joke1575,
    Joke1576,
    Joke1577,
    Joke1578,
    Joke1579,
    Joke1580,
    Joke1581,
    Joke1582,
    Joke1583,
    Joke1584,
    Joke1585,
    Joke1586,
    Joke1587,
    Joke1588,
    Joke1589,
    Joke1590,
    Joke1591,
    Joke1592,
    Joke1593,
    Joke1594,
    Joke1595,
    Joke1596,
    Joke1597,
    Joke1598,
    Joke1599,
    Joke1600,
    Joke1601,
    Joke1602,
    Joke1603,
    Joke1604,
    Joke1605,
    Joke1606,
    Joke1607,
    Joke1608,
    Joke1609,
    Joke1610,
    Joke1611,
    Joke1612,
    Joke1613,
    Joke1614,
    Joke1615,
    Joke1616,
    Joke1617,
    Joke1618,
    Joke1619,
    Joke1620,
    Joke1621,
    Joke1622,
    Joke1623,
    Joke1624,
    Joke1625,
    Joke1626,
    Joke1627,
    Joke1628,
    Joke1629,
    Joke1630,
    Joke1631,
    Joke1632,
    Joke1633,
    Joke1634,
    Joke1635,
    Joke1636,
    Joke1637,
    Joke1638,
    Joke1639,
    Joke1640,
    Joke1641,
    Joke1642,
    Joke1643,
    Joke1644,
    Joke1645,
    Joke1646,
    Joke1647,
    Joke1648,
    Joke1649,
    Joke1650,
    Joke1651,
    Joke1652,
    Joke1653,
    Joke1654,
    Joke1655,
    Joke1656,
    Joke1657,
    Joke1658,
    Joke1659,
    Joke1660,
    Joke1661,
    Joke1662,
    Joke1663,
    Joke1664,
    Joke1665,
    Joke1666,
    Joke1667,
    Joke1668,
    Joke1669,
    Joke1670,
    Joke1671,
    Joke1672,
    Joke1673,
    Joke1674,
    Joke1675,
    Joke1676,
    Joke1677,
    Joke1678,
    Joke1679,
    Joke1680,
    Joke1681,
    Joke1682,
    Joke1683,
    Joke1684,
    Joke1685,
    Joke1686,
    Joke1687,
    Joke1688,
    Joke1689,
    Joke1690,
    Joke1691,
    Joke1692,
    Joke1693,
    Joke1694,
    Joke1695,
    Joke1696,
    Joke1697,
    Joke1698,
    Joke1699,
    Joke1700,
    Joke1701,
    Joke1702,
    Joke1703,
    Joke1704,
    Joke1705,
    Joke1706,
    Joke1707,
    Joke1708,
    Joke1709,
    Joke1710,
    Joke1711,
    Joke1712,
    Joke1713,
    Joke1714,
    Joke1715,
    Joke1716,
    Joke1717,
    Joke1718,
    Joke1719,
    Joke1720,
    Joke1721,
    Joke1722,
    Joke1723,
    Joke1724,
    Joke1725,
    Joke1726,
    Joke1727,
    Joke1728,
    Joke1729,
    Joke1730,
    Joke1731,
    Joke1732,
    Joke1733,
    Joke1734,
    Joke1735,
    Joke1736,
    Joke1737,
    Joke1738,
    Joke1739,
    Joke1740,
    Joke1741,
    Joke1742,
    Joke1743,
    Joke1744,
    Joke1745,
    Joke1746,
    Joke1747,
    Joke1748,
    Joke1749,
    Joke1750,
    Joke1751,
    Joke1752,
    Joke1753,
    Joke1754,
    Joke1755,
    Joke1756,
    Joke1757,
    Joke1758,
    Joke1759,
    Joke1760,
    Joke1761,
    Joke1762,
    Joke1763,
    Joke1764,
    Joke1765,
    Joke1766,
    Joke1767,
    Joke1768,
    Joke1769,
    Joke1770,
    Joke1771,
    Joke1772,
    Joke1773,
    Joke1774,
    Joke1775,
    Joke1776,
    Joke1777,
    Joke1778,
    Joke1779,
    Joke1780,
    Joke1781,
    Joke1782,
    Joke1783,
    Joke1784,
    Joke1785,
    Joke1786,
    Joke1787,
    Joke1788,
    Joke1789,
    Joke1790,
    Joke1791,
    Joke1792,
    Joke1793,
    Joke1794,
    Joke1795,
    Joke1796,
    Joke1797,
    Joke1798,
    Joke1799,
    Joke1800,
    Joke1801,
    Joke1802,
    Joke1803,
    Joke1804,
    Joke1805,
    Joke1806,
    Joke1807,
    Joke1808,
    Joke1809,
    Joke1810,
    Joke1811,
    Joke1812,
    Joke1813,
    Joke1814,
    Joke1815,
    Joke1816,
    Joke1817,
    Joke1818,
    Joke1819,
    Joke1820,
    Joke1821,
    Joke1822,
    Joke1823,
    Joke1824,
    Joke1825,
    Joke1826,
    Joke1827,
    Joke1828,
    Joke1829,
    Joke1830,
    Joke1831,
    Joke1832,
    Joke1833,
    Joke1834,
    Joke1835,
    Joke1836,
    Joke1837,
    Joke1838,
    Joke1839,
    Joke1840,
    Joke1841,
    Joke1842,
    Joke1843,
    Joke1844,
    Joke1845,
    Joke1846,
    Joke1847,
    Joke1848,
    Joke1849,
    Joke1850,
    Joke1851,
    Joke1852,
    Joke1853,
    Joke1854,
    Joke1855,
    Joke1856,
    Joke1857,
    Joke1858,
    Joke1859,
    Joke1860,
    Joke1861,
    Joke1862,
    Joke1863,
    Joke1864,
    Joke1865,
    Joke1866,
    Joke1867,
    Joke1868,
    Joke1869,
    Joke1870,
    Joke1871,
    Joke1872,
    Joke1873,
    Joke1874,
    Joke1875,
    Joke1876,
    Joke1877,
    Joke1878,
    Joke1879,
    Joke1880,
    Joke1881,
    Joke1882,
    Joke1883,
    Joke1884,
    Joke1885,
    Joke1886,
    Joke1887,
    Joke1888,
    Joke1889,
    Joke1890,
    Joke1891,
    Joke1892,
    Joke1893,
    Joke1894,
    Joke1895,
    Joke1896,
    Joke1897,
    Joke1898,
    Joke1899,
    Joke1900,
    Joke1901,
    Joke1902,
    Joke1903,
    Joke1904,
    Joke1905,
    Joke1906,
    Joke1907,
    Joke1908,
    Joke1909,
    Joke1910,
    Joke1911,
    Joke1912,
    Joke1913,
    Joke1914,
    Joke1915,
    Joke1916,
    Joke1917,
    Joke1918,
    Joke1919,
    Joke1920,
    Joke1921,
    Joke1922,
    Joke1923,
    Joke1924,
    Joke1925,
    Joke1926,
    Joke1927,
    Joke1928,
    Joke1929,
    Joke1930,
    Joke1931,
    Joke1932,
    Joke1933,
    Joke1934,
    Joke1935,
    Joke1936,
    Joke1937,
    Joke1938,
    Joke1939,
    Joke1940,
    Joke1941,
    Joke1942,
    Joke1943,
    Joke1944,
    Joke1945,
    Joke1946,
    Joke1947,
    Joke1948,
    Joke1949,
    Joke1950,
    Joke1951,
    Joke1952,
    Joke1953,
    Joke1954,
    Joke1955,
    Joke1956,
    Joke1957,
    Joke1958,
    Joke1959,
    Joke1960,
    Joke1961,
    Joke1962,
    Joke1963,
    Joke1964,
    Joke1965,
    Joke1966,
    Joke1967,
    Joke1968,
    Joke1969,
    Joke1970,
    Joke1971,
    Joke1972,
    Joke1973,
    Joke1974,
    Joke1975,
    Joke1976,
    Joke1977,
    Joke1978,
    Joke1979,
    Joke1980,
    Joke1981,
    Joke1982,
    Joke1983,
    Joke1984,
    Joke1985,
    Joke1986,
    Joke1987,
    Joke1988,
    Joke1989,
    Joke1990,
    Joke1991,
    Joke1992,
    Joke1993,
    Joke1994,
    Joke1995,
    Joke1996,
    Joke1997,
    Joke1998,
    Joke1999,
    Joke2000,
]
