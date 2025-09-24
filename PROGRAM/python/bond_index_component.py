"""
債券指數成分資料類別

此模組實現了一個 Python class 用於表示某一天特定債券指數的債券成分資料。
包含債券基本資訊、指數相關資訊、價格與收益資訊、市場資料以及日期資訊。
"""

from datetime import datetime
from typing import Optional


class BondIndexComponent:
    """
    債券指數成分資料類別
    
    用於表示某一天特定債券指數的債券成分資料，包含所有相關的基本資訊、
    指數資訊、價格收益資訊、市場資料以及日期資訊。
    """
    
    def __init__(
        self,
        # 債券基本資訊
        bond_name: str,
        isin: str,
        issuer: str,
        credit_rating: str,
        maturity_date: datetime,
        
        # 指數相關資訊
        index_name: str,
        weight_in_index: float,
        
        # 價格與收益相關資訊
        bond_price: float,
        yield_rate: float,
        yield_to_maturity: float,
        duration: float,
        
        # 市場資料
        market_value: float,
        trading_volume: float,
        
        # 日期資訊
        data_date: datetime
    ):
        """
        初始化債券指數成分資料
        
        Args:
            bond_name: 債券名稱
            isin: ISIN國際證券識別號碼
            issuer: 發行人
            credit_rating: 信用評級
            maturity_date: 到期日
            index_name: 指數名稱
            weight_in_index: 在指數中的權重 (0-1之間的小數)
            bond_price: 債券價格
            yield_rate: 殖利率
            yield_to_maturity: 到期收益率
            duration: 期間
            market_value: 市場價值
            trading_volume: 交易量
            data_date: 資料日期
        """
        # 債券基本資訊
        self.bond_name = bond_name
        self.isin = isin
        self.issuer = issuer
        self.credit_rating = credit_rating
        self.maturity_date = maturity_date
        
        # 指數相關資訊
        self.index_name = index_name
        self.weight_in_index = weight_in_index
        
        # 價格與收益相關資訊
        self.bond_price = bond_price
        self.yield_rate = yield_rate
        self.yield_to_maturity = yield_to_maturity
        self.duration = duration
        
        # 市場資料
        self.market_value = market_value
        self.trading_volume = trading_volume
        
        # 日期資訊
        self.data_date = data_date
        
        # 基本驗證
        self._validate_data()
    
    def _validate_data(self):
        """驗證輸入資料的基本合理性"""
        if self.weight_in_index < 0 or self.weight_in_index > 1:
            raise ValueError("權重必須在 0 到 1 之間")
        
        if self.bond_price <= 0:
            raise ValueError("債券價格必須大於 0")
        
        if self.market_value <= 0:
            raise ValueError("市場價值必須大於 0")
        
        if self.trading_volume < 0:
            raise ValueError("交易量不能為負數")
        
        if self.duration < 0:
            raise ValueError("期間不能為負數")
    
    def __str__(self) -> str:
        """
        返回債券指數成分資料的格式化字符串表示
        
        Returns:
            格式化的字符串，包含所有債券相關資訊
        """
        return f"""
=== 債券指數成分資料 ===
資料日期: {self.data_date.strftime('%Y-%m-%d')}

【債券基本資訊】
債券名稱: {self.bond_name}
ISIN: {self.isin}
發行人: {self.issuer}
信用評級: {self.credit_rating}
到期日: {self.maturity_date.strftime('%Y-%m-%d')}

【指數相關資訊】
指數名稱: {self.index_name}
指數權重: {self.weight_in_index:.4%}

【價格與收益資訊】
債券價格: {self.bond_price:.2f}
殖利率: {self.yield_rate:.4%}
到期收益率: {self.yield_to_maturity:.4%}
期間: {self.duration:.2f}

【市場資料】
市場價值: {self.market_value:,.2f}
交易量: {self.trading_volume:,.0f}
"""
    
    def __repr__(self) -> str:
        """返回物件的程式碼表示"""
        return (f"BondIndexComponent(bond_name='{self.bond_name}', "
                f"isin='{self.isin}', data_date='{self.data_date.date()}')")
    
    def to_dict(self) -> dict:
        """
        將債券資料轉換為字典格式
        
        Returns:
            包含所有債券資料的字典
        """
        return {
            'bond_name': self.bond_name,
            'isin': self.isin,
            'issuer': self.issuer,
            'credit_rating': self.credit_rating,
            'maturity_date': self.maturity_date.isoformat(),
            'index_name': self.index_name,
            'weight_in_index': self.weight_in_index,
            'bond_price': self.bond_price,
            'yield_rate': self.yield_rate,
            'yield_to_maturity': self.yield_to_maturity,
            'duration': self.duration,
            'market_value': self.market_value,
            'trading_volume': self.trading_volume,
            'data_date': self.data_date.isoformat()
        }
    
    def get_days_to_maturity(self) -> int:
        """
        計算距離到期日的天數
        
        Returns:
            距離到期日的天數
        """
        return (self.maturity_date - self.data_date).days
    
    def get_weight_percentage(self) -> str:
        """
        獲取權重的百分比字符串表示
        
        Returns:
            權重的百分比字符串 (例如: "2.50%")
        """
        return f"{self.weight_in_index:.2%}"


# 範例使用方式
if __name__ == "__main__":
    # 創建一個債券指數成分資料範例
    bond_data = BondIndexComponent(
        # 債券基本資訊
        bond_name="台灣政府公債 2030",
        isin="TW0000012345",
        issuer="中華民國政府",
        credit_rating="AA+",
        maturity_date=datetime(2030, 12, 31),
        
        # 指數相關資訊
        index_name="台灣政府債券指數",
        weight_in_index=0.025,  # 2.5%
        
        # 價格與收益相關資訊
        bond_price=102.50,
        yield_rate=0.0275,  # 2.75%
        yield_to_maturity=0.0280,  # 2.80%
        duration=6.25,
        
        # 市場資料
        market_value=1025000000,  # 10.25億
        trading_volume=50000000,  # 5千萬
        
        # 日期資訊
        data_date=datetime(2024, 9, 24)
    )
    
    # 顯示債券資料
    print(bond_data)
    
    # 顯示其他資訊
    print(f"距離到期日: {bond_data.get_days_to_maturity()} 天")
    print(f"權重百分比: {bond_data.get_weight_percentage()}")
    
    # 轉換為字典格式
    bond_dict = bond_data.to_dict()
    print(f"\n字典格式: {bond_dict}")