#coding:utf8

#Author: tsuki
#Date: 2017-12-08
#Time: 22:17
from common.database.dao.mysqlSQLAlchemyBaseDao import MysqlSQLAlchemyBaseDao
from common.database.entity.cnvdEntity import CNVDEntity


class CNVDDao(MysqlSQLAlchemyBaseDao):

    def insert(self, messageResult):
        try:
            cnvd = CNVDEntity(chname = messageResult['chname'],
                              cnvd_id = messageResult['cnvd_id'],
                              release_time=messageResult['release_time'],
                              vul_level=messageResult['vul_level'],
                              impact_product=messageResult['impact_product'],
                              bugtraq_id=messageResult['bugtraq_id'],
                              cve_id = messageResult['cve_id'],
                              vul_description=messageResult['vul_description'],
                              vul_type=messageResult['vul_type'],
                              reference_link=messageResult['reference_link'],
                              vul_solution=messageResult['vul_solution'],
                              finder = messageResult['finder'],
                              vendor_patch=messageResult['vendor_patch'],
                              validation_info=messageResult['validation_info'],
                              submission_time=messageResult['submission_time'],
                              included_time=messageResult['included_time'],
                              update_time=messageResult['update_time'],
                              vul_attachment=messageResult['vul_attachment'])
            self.session.add(cnvd)
            self.session.commit()
        except Exception as excep:
            self.logger.error("insert error {}".format(excep))
            self.session.rollback()
            raise
        self.session.close()

    def selectByCNVDId(self, cnvdId):
        return self.session.query(CNVDEntity).filter_by(cnvd_id = cnvdId).all()




